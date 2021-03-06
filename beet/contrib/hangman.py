"""Plugin that provides indentation-based syntactic extensions for functions.

With this plugin, commands can spread over multiple lines by using
hanging indents. Interspersed and trailing comments are hoisted above
the current command. The plugin tries its best to keep blank lines
and retain the original formatting of the function.

The plugin also supports the "run commands" syntax suggested here:
https://feedback.minecraft.net/hc/en-us/community/posts/360077450811-In-line-functions-in-mcfunction-files
"""


__all__ = [
    "hangman",
    "parse_lines",
    "parse_trailing_comment",
    "fold_hanging_commands",
]


import re
from typing import Iterable, Iterator, List, Literal, Optional, Tuple, Union, cast

from beet import Context, Function, Plugin
from beet.core.utils import JsonDict

REGEX_COMMENT = re.compile(r"(\s+#(?:\s+.*)?$)")
REGEX_QUOTE = re.compile(r"(\"(?:.*?[^\\])?\"|'(?:.*?[^\\])?')")
REGEX_RUN_COMMANDS = re.compile(r"(\s*execute\b(?:.*)\b)run\s+commands(\s*)")
REGEX_FOLD_COMMENT = re.compile(r"\s*#\s*fold\s*:\s*(\w+)\s*")


TokenType = Union[
    Literal["TEXT"],
    Literal["BLANK"],
    Literal["COMMENT"],
    Literal["INDENT"],
    Literal["DEDENT"],
]
Token = Tuple[TokenType, str]


def beet_default(ctx: Context):
    config = ctx.meta.get("hangman", cast(JsonDict, {}))

    match = config.get("match", ())

    ctx.require(hangman(match))


def hangman(match: Iterable[str] = ()) -> Plugin:
    """Return a plugin that provides indentation-based syntactic extensions for functions."""

    def plugin(ctx: Context):
        for path in ctx.data.functions.match(*match):
            function = ctx.data.functions[path]
            function.lines = list(
                fold_hanging_commands(ctx, parse_lines(function.lines))
            )

    return plugin


def fold_hanging_commands(ctx: Context, tokens: Iterable[Token]) -> Iterator[str]:
    """Fold hanging commands on a single line."""
    tokens = iter(tokens)

    current = ""
    indent_level = 0

    for token_type, value in tokens:
        if token_type == "DEDENT":
            indent_level -= 1
            if indent_level < 0:
                break

        elif token_type == "INDENT":
            if REGEX_RUN_COMMANDS.match(current):
                key = ctx.generate(Function(list(fold_hanging_commands(ctx, tokens))))
                current = REGEX_RUN_COMMANDS.sub(fr"\1run function {key}\2", current)
            else:
                indent_level += 1

        else:
            if indent_level:
                if token_type == "TEXT":
                    current += " " + value
                elif token_type != "BLANK":
                    yield value
            else:
                if current:
                    yield current
                if token_type == "TEXT":
                    current = value
                else:
                    current = ""
                    yield value

    if current:
        yield current


def parse_lines(lines: Iterable[str]) -> Iterator[Token]:
    """Split the input lines into tokens."""
    indentation = [0]
    blanks: List[Token] = []
    fold_off = False

    for line in lines:
        if match := REGEX_FOLD_COMMENT.match(line):
            if match[1] in ["on", "off"]:
                fold_off = match[1] == "off"
            continue

        if fold_off:
            while len(indentation) > 1:
                yield "DEDENT", ""
                indentation.pop()
            yield from blanks
            blanks = []
            yield "TEXT", line
            continue

        stripped = line.lstrip()

        if not stripped:
            blanks.append(("BLANK", stripped))
            continue

        indent = len(line[: -len(stripped)].expandtabs())

        while indent < indentation[-1]:
            yield "DEDENT", ""
            indentation.pop()

        if indent > indentation[-1]:
            yield "INDENT", ""
            indentation.append(indent)

        yield from blanks
        blanks = []

        if stripped.startswith("#"):
            yield "COMMENT", stripped
        else:
            stripped, comment = parse_trailing_comment(stripped)
            if comment:
                yield "COMMENT", comment
            yield "TEXT", stripped

    while len(indentation) > 1:
        yield "DEDENT", ""
        indentation.pop()

    yield from blanks


def parse_trailing_comment(line: str) -> Tuple[str, Optional[str]]:
    """Split the line and return the extracted trailing comment."""
    chunks = REGEX_QUOTE.split(line)
    result = ""

    while chunks:
        text, *comment = REGEX_COMMENT.split(chunks.pop(0))
        result += text
        if comment:
            return result, comment[0].lstrip() + "".join(chunks)
        if chunks:
            result += chunks.pop(0)

    return result, None
