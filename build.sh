#!/bin/bash

set -e  # exits immediately on any error
set -x  # print the command before executing it

## ensure script runs from the correct dir --------------------------
DIR_NAME="bdr_dashboard_tools"
if [ "$(basename "$PWD")" != "$DIR_NAME" ]; then
  echo "Error: Run this script from the '$DIR_NAME' directory."
  exit 1
fi

## remove pre-existing build stuff ----------------------------------
rm -rf ./build
rm -f ./bdr_dashboard_tools/bdr_dashboard_tools.egg-info
rm -f ../bdr_dashboard_tools_binary

## activate the venv for access to shiv -----------------------------
source ../env/bin/activate  

## build the binary -------------------------------------------------
shiv --output-file ../bdr_dashboard_tools_binary --compressed --reproducible --console-script run_this  ./ --upgrade


## explanation...
# shiv 
#     --output-file ../hello_binary_02      # specifies the output file relative path
#     --compressed                          # compresses the output file
#     --reproducible                        # ensures that given the same input, output-file is the same
#     --console-script run_this             # defines the handle to the setup.py setup() entry_points argument
#     ./                                    # specifies the directory containing the setup.py file
#     --upgrade                             # overwrite the output file if it already exists (although in testing this already seems to happen)
