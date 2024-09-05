
# Tools

This is a collection of command-line tools packaged using `shiv`. The tools are organized into different modules, each serving a specific purpose.


## Modules

- `count_collections`: A tool for grabbing collections stats.
- `update_foo`: A tool for updating something.


## Usage — Development

```bash
$ cd /to/tools/
$ source ../venv_tools/bin/activate
(venv_tools) $ python ./code_to_package/main.py count_collections --data "bar" 
...or...
(venv_tools) $ python -m tools.main create_foo --data "bar"
```


## Usage — Binary

```bash
$ tools_binary count_collections --data "bar"
$ tools_binary update_foo --data "baz"
```


## To create, then use the binary

```bash
$ cd /to/tools/
$ bash ./build.sh
$ ../tools_binary count_collections --data "bar"
```
