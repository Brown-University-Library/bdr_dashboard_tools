
# Tools

This is a collection of command-line tools packaged using `shiv`. The tools are organized into different modules, each serving a specific purpose.


## Modules

- `count_collections`: A tool for grabbing collections stats.
- `update_foo`: A tool for updating something.


## Usage — Development

```bash
$ cd /to/bdr_dashboard_tools/
$ source ../env/bin/activate
(env) $ python ./code_to_package/main.py count_collections --data "bar" 
...or...
(env) $ python -m code_to_package.main count_collections --data "bar"
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
