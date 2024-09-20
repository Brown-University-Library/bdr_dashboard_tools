on this page...
- [Purpose](#purpose)
- [Installation](#installation)
- ["bdr_dashboard_tools" -- about](#bdr_dashboard_tools----about)
- [Architecture --> flow](#architecture----flow)
- [Sample modules](#sample-modules)
- [Usage — Development](#usage--development)
- [Usage — Binary](#usage--binary)
- [To create, and then use the binary immediately](#to-create-and-then-use-the-binary-immediately)
- [To use the binary from within python code](#to-use-the-binary-from-within-python-code)

---


## Purpose

This project was originally designed as an out-of-work side-project experiment to explore good binary "packaging" architecture/practices for related tools, using [shiv], the packager used by and supported by LinkedIn. Initially it had modules that simply printed "foo" and "bar" -- but I shifted this to actually have two simple modules that do something useful. 

Still, the purpose isn't (yet anyway) real utility, but to demo an architecture to see if it's worth pursuing/standardizing on, while we also explore other aspects of packaging, like making "import-style" packaging more useful.

[shiv]: <https://shiv.readthedocs.io/en/latest/>

Some nice features:
- if you look at the contents of the `count_collections` dir, and the `search_collection_name` dir, you'll see that their architecture is exactly the same, so it's easy to know how to add a module.
- it can be hard to know which version of a binary is in use, running `$ ../bdr_dashboard_tools_binary --version` addresses this.
- each module has it's own `--help`, ie: `bdr_dashboard_tools_binary count_collections --help`
- `setup.py` normally has a setup() function that lists the packages to be installed into the binary. This setup.py loads the required packages right from the `local.txt` file, so no need to remember to add packages to the setup.py as new modules are added! _(todo: add code to setup.py to recognize if it's being run from a dev-server, and load `staging.txt` packages if so.)_

---


## Installation

(for development purposes)

```bash
$ mkdir ./bdr_dashboard_tools_stuff
$ cd ./bdr_dashboard_tools_stuff
$ git clone git@github.com:birkin/tools.git ./bdr_dashboard_tools
$ /path/to/python3.8 -m venv ./the_venv
$ cd ./bdr_dashboard tools
$ source ../the_venv/bin/activate
(the_venv) $ pip install -r ./requirements_app/local.txt
```

_(Sensible tip: use the version of python used by the oldest server on which you'll be running the code or binary.)_

---


## "bdr_dashboard_tools" -- about

This is a collection of command-line tools packaged using `shiv`. The tools are organized into different modules, each serving a specific purpose. But really, this project is to demo a way to package different related-tools together easily.

---


### Architecture --> flow

When a command like:
```bash
(env) $ python ./code_to_package/main.py count_collections --output "columnar"
``` 

or

```bash
bdr_dashboard_tools_binary count_collections --output "columnar"
```

...is run, `code_to_package/main.py` is run. 

That file simply handles a possible `--version` flag -- or, it captures the "module" argument and its flags. It then uses the "module" argument to forward the flags to the appropriate module, ie `code_to_package/count_collections/` or `code_to_package/search_collection_name/`.

Each module has a `cli.py`, and a `manager.py` -- and likely a `utils.py`. 

When `code_to_package/main.py` hands off to a module, it hands off to the module's `cli.py`, which validates the args sent to the module. That then hands off to the manager.py's `manage_processing( argument_data )` function, which does the work, either directly, or by using helper-functions from the `utils.py` module.

---


## Sample modules

- `count_collections`: Grabs the top 100 collections, sorted by number of items within the collection.
- `search_collection_name`: Searches the BDR on the given collection-name and returns pid, url, and abstract.

---


## Usage — Development

pattern: main.py file, then module, then flags

example:

```bash
$ cd /to/bdr_dashboard_tools/
$ source ../env/bin/activate
(env) $ python ./code_to_package/main.py count_collections --output "json" 
...or...
(env) $ python -m code_to_package.main count_collections --output "json" 
```
(also takes argument `--output "columnar"`)

example using the other module:

```bash
(env) $ python ./code_to_package/main.py search_collection_name --output "json" --collection_name "Digitizing Timbuktu"
```
(also takes argument `--output "text"`)

---


## Usage — Binary

pattern: binary, then module, then flags

example:

```bash
$ bdr_dashboard_tools_binary count_collections --output "columnar"
```

example using the other module:

```bash
$ bdr_dashboard_tools_binary search_collection_name --output "text" --collection_name "Digitizing Timbuktu"
```

---


## To create, and then use the binary immediately

```bash
$ cd /to/bdr_dashboard_tools/
$ bash ./build.sh
$ ../bdr_dashboard_tools_binary count_collections --output "json"
```

That `build.sh` script runs a `shiv` command that runs the `setup.py` file.

---


## To use the binary from within python code

```
>>> import os, subprocess
>>> cmd: list = [ './bdr_dashboard_tools_binary', 'count_collections', '--output', 'columnar' ]
>>> result: subprocess.CompletedProcess = subprocess.run( cmd, capture_output=True, text=True )
>>> print( 'output:', result.stdout )
output:       
  COLLECTION                                                                                NO. ITEMS  
    
  Brown University Library                                                                  319964     
  The Gordon Hall and Grace Hoag Collection of Dissenting and Extremist Printed Propaganda  217369     
  Biology and Medicine                                                                      73827      
  ... [snip] ...        

Total number of collections: 100

>>> print( 'error:', result.stderr )
error: 
```

Say you want to run code that has envars loaded from a dotenv. The binary, as run above, won't see those envars. Here's how to handle that (the binary currently doesn't need any envars):

```
>>> import os, subprocess
>>> cmd: list = [ './bdr_dashboard_tools_binary', 'count_collections', '--output', 'columnar' ]
>>> binary_env: dict = os.environ.copy()
>>> result: subprocess.CompletedProcess = subprocess.run( cmd, env=binary_env, capture_output=True, text=True )
>>> print( 'output:', result.stdout )
output:       
  COLLECTION                                                                                NO. ITEMS  
    
  Brown University Library                                                                  319964     
  The Gordon Hall and Grace Hoag Collection of Dissenting and Extremist Printed Propaganda  217369     
  Biology and Medicine                                                                      73827      
  ... [snip] ...        

Total number of collections: 100

>>> print( 'error:', result.stderr )
error: 
```

I said above that the binary doesn't currently _need_ any envars. That's true. But it _can_ use one.
Say, like above, you want to run code that has envars loaded from a dotenv, and you want the binary to have access to them... but you want to change an envar sent to the binary:
 
```
>>> import os, subprocess
>>> cmd: list = [ './bdr_dashboard_tools_binary', 'count_collections', '--output', 'columnar' ]
>>> binary_env: dict = os.environ.copy()
>>> binary_env['BDT__LOGLEVEL'] = 'DEBUG'
>>> result: subprocess.CompletedProcess = subprocess.run( cmd, env=binary_env, capture_output=True, text=True )
>>> print( 'output:', result.stdout )
output:       
  COLLECTION                                                                                NO. ITEMS  
    
  Brown University Library                                                                  319964     
  The Gordon Hall and Grace Hoag Collection of Dissenting and Extremist Printed Propaganda  217369     
  Biology and Medicine                                                                      73827      
  ... [snip] ...        

Total number of collections: 100

>>> print( 'error:', result.stderr )
error: [19/Sep/2024 22:20:58] DEBUG [main-<module>()::19] sys-path:, ``['./bdr_dashboard_tools_binary',
 '/opt/homebrew/Cellar/python@3.8/3.8.19/Frameworks/Python.framework/Versions/3.8/lib/python38.zip',
 '/opt/homebrew/Cellar/python@3.8/3.8.19/Frameworks/Python.framework/Versions/3.8/lib/python3.8',
 ... [snipping LOTS of debug output] ...
 ```

---
