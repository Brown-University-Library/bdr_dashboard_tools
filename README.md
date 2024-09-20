## Purpose

This project was originally designed as an out-of-work side-project experiment to explore good binary "packaging" architecture/practices for related tools, using [shiv], the packager used by and supported by LinkedIn. Initially it had modules that simply printed "foo" and "bar" -- but I shifted this to actually have two simple modules that do something useful.

[shiv]: <https://shiv.readthedocs.io/en/latest/>

Some nice features:
- if you look at the contents of the `count_collections` dir, and the `search_collection_name` dir, you'll see that their architecture is exactly the same, so it's easy to know how to add a module.
- it can be hard to know which version of a binary is in use, running `$ ../bdr_dashboard_tools_binary --version` addresses this.
- each module has it's own `--help`, ie: `bdr_dashboard_tools_binary count_collections --help`
- `setup.py` normally has a setup() function that lists the packages to be installed. This setup.py loads the required packages right from the `local.txt` file, so no need to remember to add packages to the setup.py as new modules are added! _(todo: add code to setup.py to recognize if it's being run from a dev-server, and load `staging.txt` packages if so.)_


## Installation

(for development purposes)

```bash
$ mkdir ./bdr_dashboard_tools_stuff
$ cd ./bdr_dashboard_tools_stuff
$ /path/to/python3.8 -m venv ./the_venv
(the_venv) $ pip install -r ./requirements_app/local.txt
```

_(Sensible tip: use the version of python used by the oldest server on which you'll be running the code or binary.)_


## bdr_dashboard_tools -- about

This is a collection of command-line tools packaged using `shiv`. The tools are organized into different modules, each serving a specific purpose. But really, this project is to demo a way to package different related-tools together easily.

### Architecture

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



## Sample modules

- `count_collections`: Grabs the top 100 collections, sorted by number of items within the collection.
- `search_collection_name`: Searches the BDR on the given collection-name and returns pid, url, and abstract.


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


## To create, and then use the binary

```bash
$ cd /to/bdr_dashboard_tools/
$ bash ./build.sh
$ ../bdr_dashboard_tools_binary count_collections --output "json"
```

That `build.sh` script runs a `shiv` command that runs the `setup.py` file.
