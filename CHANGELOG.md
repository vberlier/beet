# Changelog

<!--next-version-placeholder-->

## v0.22.5 (2021-05-07)
### Fix
* Don't reload modules from site-packages ([`de2ecab`](https://github.com/mcbeet/beet/commit/de2ecab29b22dd0cd72edb368d709868a6fe5e9e))

## v0.22.4 (2021-05-07)
### Fix
* Make hangman plugin configurable ([`cc56cd8`](https://github.com/mcbeet/beet/commit/cc56cd8116d650376aa4f052255691ae869e375a))

### Documentation
* Add file handles overview ([`f6741ac`](https://github.com/mcbeet/beet/commit/f6741ac63d3dbb12379e2df16f2c6c1bf4923b4a))

## v0.22.3 (2021-05-05)
### Fix
* Add defaults for everything ([`f229b3c`](https://github.com/mcbeet/beet/commit/f229b3c2bcba413008600fc38116ad0eede95eee))
* Tweak pack and namespace equality ([`5906fb2`](https://github.com/mcbeet/beet/commit/5906fb2e6632a845ffe6364c9785ba02ee80ea20))
* Rename pack image ([`a3007a1`](https://github.com/mcbeet/beet/commit/a3007a158875178b064aae50b384871c6f31adc7))

### Documentation
* Start writing general overview ([`fd9348d`](https://github.com/mcbeet/beet/commit/fd9348d11f7d7513ce0fd3e31864a5216880f047))

## v0.22.2 (2021-05-04)
### Fix
* Use custom PathLike ([`b569367`](https://github.com/mcbeet/beet/commit/b569367f472e4d95f1c28dc3162a49be06b602e4))

### Documentation
* Update README ([`ab8056b`](https://github.com/mcbeet/beet/commit/ab8056b8c186460a59d969faa1a81af322954421))

## v0.22.1 (2021-05-02)
### Fix
* Keep template globals across environment resets ([`02379e2`](https://github.com/mcbeet/beet/commit/02379e2f1e7b043e02b570e41ce05b1d6ab2cd87))

## v0.22.0 (2021-04-27)
### Feature
* Make it possible to temporarily disable folding ([`489ad7c`](https://github.com/mcbeet/beet/commit/489ad7c65643c14633358396389dedc7d96a4d8d))
* Add particles ([`adaaf0d`](https://github.com/mcbeet/beet/commit/adaaf0d9fbdd69bbfde42a3cf24c632b0c135d36))
* Add sounds ([`6d88263`](https://github.com/mcbeet/beet/commit/6d88263228174fa21d594398210c026d00a7130e))
* Add namespace extra ([`bd7b148`](https://github.com/mcbeet/beet/commit/bd7b1480df469fdeaf1a9ce1bf6b27051e758c24))

## v0.21.0 (2021-04-23)
### Feature
* Expose generate_path in templates ([`9354b78`](https://github.com/mcbeet/beet/commit/9354b78a3fe73d513e0b3a287d6fd0c7944d13b2))
* Add generate.function_tree() ([`f9aac53`](https://github.com/mcbeet/beet/commit/f9aac53c2d1c46076faf270bad85317a9f856911))
* Add TreeNode.root ([`0f0078f`](https://github.com/mcbeet/beet/commit/0f0078f8b182cf9df492e1281727b3d686e33865))
* Add generate.path() ([`80d2689`](https://github.com/mcbeet/beet/commit/80d26892a42fd6c7052f3041659bafbab7957b4f))
* Make it possible to specify a node key ([`2b0595e`](https://github.com/mcbeet/beet/commit/2b0595e3ee34847eceb9e6bfef725ee15eaf78d5))
* Add generate_tree ([`d37df14`](https://github.com/mcbeet/beet/commit/d37df14d6c6b45579fb64b2f7b254ac1bdd1d076))
* Output the commands in-place when the path matches the current function ([`dff5d51`](https://github.com/mcbeet/beet/commit/dff5d51a87b031557b374c669c54ca827ecf734f))
* Add beet.contrib.template_context ([`12bc6ef`](https://github.com/mcbeet/beet/commit/12bc6ef83ce62f03b6238abae351259a94c32fc0))
* Add beet.contrib.template_sandbox ([`55fbe92`](https://github.com/mcbeet/beet/commit/55fbe92c8a04d04f4696323ce4605536be3afa73))
* Ctx is no longer exposed to templates ([`00ca7e9`](https://github.com/mcbeet/beet/commit/00ca7e97513aa2638fb5cf27e48186e661b93015))
* Inject can now import services on the fly ([`edfe5af`](https://github.com/mcbeet/beet/commit/edfe5af659f4deda69c99a08ea2526d72eccc13d))
* Add prepend and append to inline_function plugin ([`e12347f`](https://github.com/mcbeet/beet/commit/e12347f1b4b96a64dc8ee5348a4d5a85b5964977))
* Add generate(render=) and make hash lowercase ([`a08c73c`](https://github.com/mcbeet/beet/commit/a08c73c8cd8bb9efc8513092cdc4c78dc07206c2))
* Render_file template source_path fallback ([`666b697`](https://github.com/mcbeet/beet/commit/666b697b5e3bb01a7093c5a589896124204833d7))
* Add generate.push() ([`40b7680`](https://github.com/mcbeet/beet/commit/40b7680465f4a0bd7888d5a9b0dba61fee8f3712))

## v0.20.1 (2021-04-22)
### Fix
* Join generate argument with current template ([`074ee28`](https://github.com/mcbeet/beet/commit/074ee288bfdf2e94af344363e511a59cd9c61572))

## v0.20.0 (2021-04-17)
### Feature
* Add generate.objective() and beet.contrib.scoreboard ([`6a5376a`](https://github.com/mcbeet/beet/commit/6a5376a237a6669283aa79885a0c21998e389b71))
* Add id and hash generate helpers ([`00cd667`](https://github.com/mcbeet/beet/commit/00cd667f94701ecffe4e31f1c8eaf1cbd923e54b))

### Fix
* Default generate.id() to {incr} ([`4429ff6`](https://github.com/mcbeet/beet/commit/4429ff6a69a3f56e94b2650897313e1aac7c6901))
* Propagate generator type and forgot return annotation for hash() ([`b1b1766`](https://github.com/mcbeet/beet/commit/b1b1766dc78bd651a8065a1d11252a2bcceb1e46))
* Don't increment registry keys unless {incr} is present ([`9786c36`](https://github.com/mcbeet/beet/commit/9786c369fa4bf3ff28d2ef5fb4dbb7263ae01f87))

## v0.19.1 (2021-04-02)
### Fix
* **generator:** Only default to content hash if hash wasn't explicitly provided ([`bee1df4`](https://github.com/mcbeet/beet/commit/bee1df4d1ea1ed12de8150c87043915f70ef5372))

## v0.19.0 (2021-03-29)
### Feature
* Make generator prefix and namespace configurable and add tests ([`4972534`](https://github.com/mcbeet/beet/commit/4972534239f1a994c3382f16973f08cecebadf0b))
* Refactor hangman plugin to support run commands syntax ([`849697b`](https://github.com/mcbeet/beet/commit/849697b4f62be42dade6e5ac6c728a156a6c583b))
* Add context generator ([`09eb6ab`](https://github.com/mcbeet/beet/commit/09eb6ab4bbaf8de0dc9ed968fc6d277a7eb0c07b))
* Add file default value ([`205c9ff`](https://github.com/mcbeet/beet/commit/205c9ff16b060ea91ab1b5eda0c1de9583ca5e6b))

## v0.18.0 (2021-03-27)
### Feature
* Add ignore_name test utility ([`e5ee8f2`](https://github.com/mcbeet/beet/commit/e5ee8f22791a8fa500a5f6093ec95ea00ef4fe51))

## v0.17.3 (2021-03-27)
### Fix
* Prevent explanation from crashing when assertrepr_compare returns None ([`0ed03ed`](https://github.com/mcbeet/beet/commit/0ed03ed8c5180455934d0bc90e294391b059e04f))

### Documentation
* Add changelog page ([`3c554ac`](https://github.com/mcbeet/beet/commit/3c554ac03be1ef71b94c52ea28ee7e404031b86a))

## v0.17.2 (2021-03-24)
### Fix
* **hangman:** Handle trailing comments ([`ff7ba22`](https://github.com/mcbeet/beet/commit/ff7ba225a099f6e5c3b5b22fb3bcfab7114acfe6))

## v0.17.1 (2021-03-24)
### Fix
* Remove dedent extension ([`ab0797a`](https://github.com/mcbeet/beet/commit/ab0797af365e9c77d6c0bf62234c232c137785bf))

## v0.17.0 (2021-03-24)
### Feature
* Add hangman plugin ([`2a96811`](https://github.com/mcbeet/beet/commit/2a96811892ad0bd4d4f858b973f10bff794eabdf))

### Documentation
* Update homepage ([`3a25a4c`](https://github.com/mcbeet/beet/commit/3a25a4cba0ca15b05b09d1e1ec8f134aefc9e0f3))
* Update ([`825181b`](https://github.com/mcbeet/beet/commit/825181bfe51abfb59d5658e38d4be67c9833d33f))
* Update cli help text ([`6093b61`](https://github.com/mcbeet/beet/commit/6093b61180031560aab4f04ba65cc75860aa9b2b))
* Add action ([`579ea4f`](https://github.com/mcbeet/beet/commit/579ea4f177f045ea3fc2d096c7d04f91de60a4ba))

## v0.16.0 (2021-03-21)
### Feature
* Support core shaders ([`69e3d19`](https://github.com/mcbeet/beet/commit/69e3d1928891891b26408ca50f6faa558df629c1))

### Fix
* Better file comparisons with source_path fast path ([`3c12aa7`](https://github.com/mcbeet/beet/commit/3c12aa7bee647d411393711e869d99f40713effe))
* Properly display edited filename on windows ([`e3c1890`](https://github.com/mcbeet/beet/commit/e3c189035d155a234aff9a9beed4caf950040e3e))

### Breaking
* ShaderProgram was renamed to Shader  ([`69e3d19`](https://github.com/mcbeet/beet/commit/69e3d1928891891b26408ca50f6faa558df629c1))

## v0.15.0 (2021-03-19)
### Feature
* Add logging ([`6505cbb`](https://github.com/mcbeet/beet/commit/6505cbb47feed1d0c4934468b67e2bd9be4aafe9))
* Add babelbox plugin ([`70e1829`](https://github.com/mcbeet/beet/commit/70e1829de45e61400c9dfcd3698ef10b41091be7))
* Add workers ([`eacd2ae`](https://github.com/mcbeet/beet/commit/eacd2ae4a6bad9fdc018f3849b748c12e9b91946))

### Fix
* Compare data for equality for json files ([`298e2e1`](https://github.com/mcbeet/beet/commit/298e2e1989d90d11dc7706c5d24e8741a86901af))

## v0.14.0 (2021-03-18)
### Feature
* Support language files and custom languages ([`abec2b1`](https://github.com/mcbeet/beet/commit/abec2b1b4f2fc27ff6b0ddf84fb9ace81834c104))

### Fix
* Only modify sys.path if the directory is not already present ([`8575d31`](https://github.com/mcbeet/beet/commit/8575d31b14c71063479af584715cfe9e7c92086f))

### Breaking
* rename pin descriptors  ([`abec2b1`](https://github.com/mcbeet/beet/commit/abec2b1b4f2fc27ff6b0ddf84fb9ace81834c104))

## v0.13.0 (2021-03-14)
### Feature
* Add plugin autoload ([`9cac58e`](https://github.com/mcbeet/beet/commit/9cac58e2ea5348509fde32ccfbd3e71a5c503678))
* Make cli extensible ([`9adb10c`](https://github.com/mcbeet/beet/commit/9adb10c5664362fb782a417eaf7b8aaf784e7e5c))

### Fix
* Don't crash when there are no entry points ([`85f6bd7`](https://github.com/mcbeet/beet/commit/85f6bd7408c98cc02b03a2a28165da2c576b42fb))

## v0.12.0 (2021-03-09)
### Feature
* Add sandstone plugin ([`cad9101`](https://github.com/mcbeet/beet/commit/cad910153131315097a6cf65f35a396ddfa525f9))

## v0.11.2 (2021-03-09)
### Fix
* Accept ProjectConfig instances for run_beet ([`9939b10`](https://github.com/mcbeet/beet/commit/9939b107c3e6dadc5e3fc8cdaba34bd06b019a53))

## v0.11.1 (2021-03-03)
### Fix
* Ignore click exceptions in error_handler ([`9544765`](https://github.com/mcbeet/beet/commit/95447651b9c40a46484d8edafc4145b587369509))

## v0.11.0 (2021-03-03)
### Feature
* Add pytest plugin for rich explanations ([`947a6b5`](https://github.com/mcbeet/beet/commit/947a6b5fe251fe630afa326e62e365d5ebaca990))
* Add whitelist ([`f5730ba`](https://github.com/mcbeet/beet/commit/f5730ba152921b64afbe4c629553c182815a7877))

## v0.10.5 (2021-02-27)
### Fix
* Overload getitem to return namespaceproxy ([`6b0b731`](https://github.com/mcbeet/beet/commit/6b0b731c77253d7cf335cda09b778feee61045d8))

## v0.10.4 (2021-02-25)
### Fix
* Change path and save ([`ecc6593`](https://github.com/mcbeet/beet/commit/ecc659385bb64fa884a01648e2f0db553542160a))

## v0.10.3 (2021-02-25)
### Fix
* Turn run_beet() into a context manager ([`852cebb`](https://github.com/mcbeet/beet/commit/852cebbb71a09be66d318cd5ce6d2f8c9d6ffb7a))

## v0.10.2 (2021-02-25)
### Fix
* Add download method ([`7951470`](https://github.com/mcbeet/beet/commit/7951470a5f7be4973816b686b311e52fd29f9a32))

## v0.10.1 (2021-02-25)
### Fix
* Use plain list to hold commands ([`9b02b77`](https://github.com/mcbeet/beet/commit/9b02b7711e3e63596f6250984a320059b6e47156))

## v0.10.0 (2021-02-24)
### Feature
* Add cache.get_path() ([`f72b51c`](https://github.com/mcbeet/beet/commit/f72b51c8aa617ff1e923fc8cad6b3f75c0566299))

### Documentation
* Add custom domain ([`899d09f`](https://github.com/mcbeet/beet/commit/899d09f0e33ab45589ffb65849abf8c8d8ae1569))
* Fix malformed table ([`3dd0a15`](https://github.com/mcbeet/beet/commit/3dd0a15ffcf9deb289e0a630d838dc0c21944251))

## v0.9.4 (2021-02-23)
### Fix
* Add 1.17 item modifiers ([`9463ac8`](https://github.com/mcbeet/beet/commit/9463ac857d36044563f712f890662720b4123608))

### Documentation
* Add toolchain ([`a6abf05`](https://github.com/mcbeet/beet/commit/a6abf0522a76e3121b6125879ae85e1c355f7e6c))

## v0.9.3 (2021-02-22)
### Fix
* Take into account pack.mcmeta in pack bool() ([`62af388`](https://github.com/mcbeet/beet/commit/62af3881a898eb4a260abeffb460df4e1d2d055e))

## v0.9.2 (2021-02-21)
### Fix
* Annotate descriptors ([`4e47cc6`](https://github.com/mcbeet/beet/commit/4e47cc6dc612eb0f804dc8f24454f5f590a24544))

## v0.9.1 (2021-02-20)
### Fix
* Make it possible to specify an existing cache and use run_beet in examples ([`5cdea1d`](https://github.com/mcbeet/beet/commit/5cdea1d46d36a4324582232a6773edefcadb4350))

## v0.9.0 (2021-02-20)
### Feature
* Add run_beet helper function ([`a2cb545`](https://github.com/mcbeet/beet/commit/a2cb5454972f768b215248fbc95575fd26a34dfc))

## v0.8.2 (2021-02-20)
### Fix
* Overload merge to automatically merge pack extras too ([`a586ee3`](https://github.com/mcbeet/beet/commit/a586ee30eb00aadb0276a6bb7b2c4b2a637ed236))

## v0.8.1 (2021-02-18)
### Fix
* Add FormattedPipelineException and use config_error_handler in subproject ([`49895e3`](https://github.com/mcbeet/beet/commit/49895e34246f39529dd984cec434863977be5da8))

## v0.8.0 (2021-02-18)
### Feature
* Remove __render__ and expose render path and render group in meta ([`adc9452`](https://github.com/mcbeet/beet/commit/adc945207098bdf4eed7699cd01a855ad899e846))
* Add ctx.override to temporarily change meta ([`c1483d0`](https://github.com/mcbeet/beet/commit/c1483d08244ed159f055d18ab487191b40a49cde))
* Expose renderer as a standalone plugin ([`e935383`](https://github.com/mcbeet/beet/commit/e935383abf7f8de9db0a7ce354b50fa78eca45fb))
* Add sandbox ([`bd538af`](https://github.com/mcbeet/beet/commit/bd538af938b740c07a1f1bdf6834816f4c476e51))
* Add explicit activate context manager ([`1e21f66`](https://github.com/mcbeet/beet/commit/1e21f66fa8068cc7309951f9924dce85ab27b333))

### Fix
* Replace exception_fallthrough with PipelineFallthroughException ([`35ace13`](https://github.com/mcbeet/beet/commit/35ace13821338f699a3426858c3b2257fbf2e73e))
* Set ctx template global in __post_init__ ([`96d928b`](https://github.com/mcbeet/beet/commit/96d928b6a81f1f272930b2ed30eac082ff455e66))
* Expose the template directories ([`7d6f7a1`](https://github.com/mcbeet/beet/commit/7d6f7a1b009770984515b09550bc36e0c7b39d96))
* Ignore cache relative to the resolved directory ([`3e77d79`](https://github.com/mcbeet/beet/commit/3e77d7929b5c2c3b71c994f52b19e2dccafbdbff))

### Documentation
* Document ctx.activate() and ctx.override() ([`286eca2`](https://github.com/mcbeet/beet/commit/286eca20b7d5b0ab64ff74048f0f8c1ecaef5e2e))

## v0.7.0 (2021-02-16)
### Feature
* Add lantern_load plugin ([`7118f10`](https://github.com/mcbeet/beet/commit/7118f10f49e574b8701004fdcc5f30dc56e89167))

## v0.6.1 (2021-02-13)
### Fix
* Make it possible to use text components and override the description in plugins ([`ad972d0`](https://github.com/mcbeet/beet/commit/ad972d011f10e7006d34c07a37f8116f7bc2227f))

## v0.6.0 (2021-02-13)
### Feature
* Add subproject helper ([`d604179`](https://github.com/mcbeet/beet/commit/d60417924b44284dac45d5ad4b23d4b5a08aee99))

### Documentation
* Add link to pipeline configuration video ([`811d426`](https://github.com/mcbeet/beet/commit/811d426ebe5943b683e957a2e98e97a8522b3122))
* Add docstring to context inject method ([`2f09ffe`](https://github.com/mcbeet/beet/commit/2f09ffe591612246c23d8997467630aa79002c75))

## v0.5.1 (2021-01-27)
### Fix
* Expose project metadata in context ([`a04081c`](https://github.com/mcbeet/beet/commit/a04081ce23c941bd240ff1187fc40645fce7e627))
* Better dotted pack name handling ([`79fccff`](https://github.com/mcbeet/beet/commit/79fccfff9d92353cebbdc631b6ae56b2e6a99be3))

## v0.5.0 (2021-01-23)
### Feature
* Add beet.contrib.minify_functions plugin ([`a7774a9`](https://github.com/mcbeet/beet/commit/a7774a9b799eac7eceb078759e02b8714da9d9c1))
* Add beet.contrib.minify_json plugin ([`78cd972`](https://github.com/mcbeet/beet/commit/78cd9728401570ad772a3684577667c126eef0a9))

### Fix
* Typo in serialization descriptor ([`edbe174`](https://github.com/mcbeet/beet/commit/edbe1740bd9bb0b85877746f693f3ba7247bbf57))

### Documentation
* Add link to plugins basics video ([`3d7a3db`](https://github.com/mcbeet/beet/commit/3d7a3dbceefeb4afc998a2599f02c441016c8c31))

## v0.4.0 (2021-01-14)
### Feature
* Handle resource pack fonts and tweak docstrings ([`57cce73`](https://github.com/mcbeet/beet/commit/57cce7380a2f9b9a15a61bac4d824e2d6ce48a2f))
* Add shaders ([`34505d9`](https://github.com/mcbeet/beet/commit/34505d99e9b6714c593a4a5f5b919d22dacd6fa2))
* Locate_minecraft() now takes into account the MINECRAFT_PATH environment variable ([`ad6668b`](https://github.com/mcbeet/beet/commit/ad6668b639a8ed6eba18cff1a41b11666b2db488))

### Fix
* Also look for the .minecraft folder in the launcher files on linux ([`5645789`](https://github.com/mcbeet/beet/commit/564578935b25193a2cbbcf8e71f44d942336a5b7))
* Strip extra underscores from normalized name ([`55b8494`](https://github.com/mcbeet/beet/commit/55b8494248098aa532fa816b0abdf6d46b236021))

## v0.3.3 (2021-01-10)
### Fix
* Tweak typing for merge implementation ([`8efa444`](https://github.com/mcbeet/beet/commit/8efa444ccf67dd25eb1fd23d4e89f07407bf404c))

### Documentation
* Add link to library overview video ([`4f37a74`](https://github.com/mcbeet/beet/commit/4f37a7496d863b0535b39a1b6c1ad3df786bc89b))

## v0.3.2 (2020-12-29)
### Fix
* Use forward slash for zipfile paths on windows ([`b605c07`](https://github.com/mcbeet/beet/commit/b605c07a06106fd97866b9c442b39313381aabb5))

### Documentation
* Link to command-line video ([`1f45b03`](https://github.com/mcbeet/beet/commit/1f45b036c55902d1736f1f63cc26202291f29842))
* Add quick start to readme ([`3310d16`](https://github.com/mcbeet/beet/commit/3310d16d5490c9554c40acb0c4d295b4d8e10e68))

## v0.3.1 (2020-12-22)
### Fix
* Default match shouldn't match anything ([`6f01d6a`](https://github.com/mcbeet/beet/commit/6f01d6a19d63d9374e575942cf40dc1b14a4df88))

## v0.3.0 (2020-12-22)
### Feature
* Add function_header plugin ([`bb73eee`](https://github.com/mcbeet/beet/commit/bb73eeef0d984ca80cfd378ab2b0a99d89a33d47))

### Fix
* Rename inline plugins ([`a6b7aaa`](https://github.com/mcbeet/beet/commit/a6b7aaa60d97bf203d771861effc0ee61425786d))

### Documentation
* Add module docstring to inline plugins ([`d829d89`](https://github.com/mcbeet/beet/commit/d829d89c815c15b34dd51ac6e3a68d563906b3c4))

## v0.2.2 (2020-12-21)
### Fix
* Trigger release to update readme ([`d409af5`](https://github.com/mcbeet/beet/commit/d409af56d4c82da5d3c2743a158128cb4ed0b062))

### Documentation
* Start writing docs ([`034c662`](https://github.com/mcbeet/beet/commit/034c662878c88d2da84c71f15d46e85c38e2e5db))
* Update readme ([`58c9822`](https://github.com/mcbeet/beet/commit/58c98226b091f3dd5994888bfdd71301dafb278f))
* Add mudkip ([`fb3cfdd`](https://github.com/mcbeet/beet/commit/fb3cfddee1b220e055659393e9ce747fddcd5a26))

## v0.2.1 (2020-12-21)
### Fix
* Include better dependencies for windows ([`b28977f`](https://github.com/mcbeet/beet/commit/b28977f206bd48b0cdae67ac1dad2e17ade81f24))

### Documentation
* Fix main branch ([`74ac998`](https://github.com/mcbeet/beet/commit/74ac998c7103ebdb9c95058e141ab1acc703670b))

## v0.2.0 (2020-12-21)
### Feature
* Trigger first automatic release ([`a5664b3`](https://github.com/mcbeet/beet/commit/a5664b3fa7f7fc6c9d1d93f1cc26f91504dd3dae))
