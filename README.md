Under development...

Next...
- try to add `--version` build-step.
- possibly update "search_collection_name" to take input from json-output of "count_collections"

---
---


# Tools

This is a collection of command-line tools packaged using `shiv`. The tools are organized into different modules, each serving a specific purpose.


## Modules

- `count_collections`: A tool for grabbing collections stats.
- `update_foo`: A tool for updating something.


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


## Usage — Binary

pattern: binary, then module, then flags

example:

```bash
$ bdr_dashboard_tools_binary count_collections --output "json"
```

example using the other module:

```bash
$ bdr_dashboard_tools_binary search_collection_name --output "text" --collection_name "Digitizing Timbuktu"
```


## To create, then use the binary

```bash
$ cd /to/bdr_dashboard_tools/
$ bash ./build.sh
$ ../bdr_dashboard_tools_binary count_collections --output "json"
```
