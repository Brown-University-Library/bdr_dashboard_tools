
# Tools

This is a collection of command-line tools packaged using `shiv`. The tools are organized into different modules, each serving a specific purpose.

## Modules

- `create_foo`: A tool for creating something.
- `update_foo`: A tool for updating something.

## Usage

After packaging with `shiv`, you can run the tools as follows:

```bash
$ tools create_foo --data "bar"
$ tools update_foo --data "baz"
```

## Development Usage

$ cd /to/tools_stuff
$ source ./env/bin/activate
(venv_tools) $ python -m tools.main create_foo --data "bar"

---
