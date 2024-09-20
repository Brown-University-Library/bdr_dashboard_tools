"""
- This script builds an executable stand-alone binary; see the readme for usage instructions.
- This script is run by the `build.sh` script. Specifically, the shiv command in the build.sh script triggers this.
"""
import re, subprocess
from setuptools import setup, find_packages


## helpers begin ----------------------------------------------------


def prep_git_commit_hash() -> None:
    """ Helper which gets and returns the commit hash of the current repository. 
        The commit has is later written to a file called commit_info.py -- which is imported in the main.py file,
            and used to display the version of the package when the --version flag is passed to the command line.    
        Called when setup.py is run, which is triggered by the shiv command in the build.sh script."""
    try:
        commit_hash = subprocess.check_output( ['git', 'rev-parse', 'HEAD'] ).strip().decode( 'utf-8' )
        with open('./code_to_package/commit_info.py', 'w') as f:
            f.write( f"COMMIT_HASH = '{commit_hash}'\n" )
    except Exception as e:
        msg = f'Error obtaining git commit hash: {e}'
        raise Exception( msg )


def get_required_packages_from_local_txt(local_txt_path: str) -> list:
    """ Parses the local.txt file and extract required packages. 
        TODO: Update the code so that it'll recognize being run on the dev-server, 
              in which case it'll use the requirements/staging.txt file."""
    regex = re.compile(r'^[a-zA-Z0-9\-_]+==[0-9]+\.[0-9]+(\.[0-9]+)?')
    with open(local_txt_path, 'r') as f:
        content = f.readlines()
    required_packages = [line.strip() for line in content if regex.match(line)]
    return required_packages
    

## helpers end ------------------------------------------------------


## ok, let's get to work --------------------------------------------


## handle the commit hash -------------------------------------------
print( 'prepping git commit hash...' )
commit_hash = prep_git_commit_hash()
print( 'git commit hash prepped.' )

## prep list of packages to install ---------------------------------
loaded_install_requires = get_required_packages_from_local_txt('./requirements_app/local.txt')

## setup() ----------------------------------------------------------
setup(
    name='bdr_dashboard_tools',
    version='1.2.3',  # not using this; the --version flag will display the commit hash... hmmm, does this require an float? i _could_ put the commit hash here!
    description='Various BDR-related tools.',
    py_modules=['main', 'commit_info'],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['run_this=code_to_package.main:main'],
    },
    install_requires=loaded_install_requires,
)
