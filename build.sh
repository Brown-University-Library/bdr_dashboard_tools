#!/bin/bash

set -e  # exits immediately on any error
set -x  # print the command before executing it

## check that the script is running from the correct directory
DIR_NAME="bdr_dashboard_tools"
if [ "$(basename "$PWD")" != "$DIR_NAME" ]; then
  echo "Error: Run this script from the '$DIR_NAME' directory."
  exit 1
fi

source ../env/bin/activate  # so we have access to shiv

shiv --output-file ../bdr_dashboard_tools_binary --compressed --reproducible --console-script run_this  ./ --upgrade


## explanation...
# shiv 
#     --output-file ../hello_binary_02      # specifies the output file relative path
#     --compressed                          # compresses the output file
#     --reproducible                        # ensures that given the same input, output-file is the same
#     --console-script run_this             # defines the handle to the setup.py setup() entry_points argument
#     ./                                    # specifies the directory containing the setup.py file
#     --upgrade                             # overwrite the output file if it already exists (although in testing this already seems to happen)
