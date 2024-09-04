
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

---


## Development Usage

$ cd /to/tools_stuff
$ source ./env/bin/activate
(venv_tools) $ python -m tools.main create_foo --data "bar"

---


## Optional: To create binary


(from ./tools_stuff/)  

```
% shiv --console-script main --output-file ./tools_binary ./tools
```

The same command, with explanatory info...

```
% shiv \
  --console-script run_this \  # tells shiv to use the entry point defined as "run_this" in the setup.py's `console_scripts` section, in this case, to run the `main()` function from `tools/main.py`.
  --output-file ./tools_binary \  # binary output path
  ./tools  # the path containing `setup.py`
```

This command creates the binary `tools_binary`, in the outer "stuff" directory, which can put anywhere and be called by another script. Note that the binary should be saved outside of the git-directory so that there is no new `git commit` to execute. This allows the binary to be run with the `--version` flag, and for the version to match the current commit.
