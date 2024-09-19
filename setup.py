# from setuptools import setup, find_packages

import re, subprocess
from setuptools import setup, find_packages


## helpers begin ----------------------------------------------------


def get_git_commit_hash() -> str:
    """ Helper which gets and returns the commit hash of the current repository. 
        The commit has is later written to a file called commit_info.py -- which is imported in the main.py file,
            and used to display the version of the package when the --version flag is passed to the command line.    
        Called when setup.py is run, which is triggered by the shiv command in the build.sh script."""
    try:
        commit_hash = subprocess.check_output( ['git', 'rev-parse', 'HEAD'] ).strip().decode( 'utf-8' )
        return commit_hash
    except Exception as e:
        msg = f'Error obtaining git commit hash: {e}'
        raise Exception( msg )


class InstallRequiresHelper:
    """ Helper class which:
        - parses the local.txt file to determine required packages.
        - compares the `initial_install_requires` list with the required packages from local.txt.
        - updates setup.py's setup() `install_requires` list, if necessary. """

    def __init__(self, local_txt_path: str, initial_install_requires: list):
        self.local_txt_path = local_txt_path
        self.install_requires = initial_install_requires

    def get_required_packages_from_local_txt(self) -> list:
        """ Parses the local.txt file and extract required packages. """
        regex = re.compile(r'^[a-zA-Z0-9\-_]+==[0-9]+\.[0-9]+(\.[0-9]+)?')
        with open( self.local_txt_path, 'r' ) as f:
            content = f.readlines()
        required_packages = [ line.strip() for line in content if regex.match(line) ]
        return required_packages

    def update_install_requires_if_necessary(self) -> list:
        """ Updates self.install_requires list with any required-packages from the requirements.txt file. 
            Returns the list. """
        required_packages_from_requirements_txt = self.get_required_packages_from_local_txt()
        missing_packages = [ pkg for pkg in required_packages_from_requirements_txt if pkg not in self.install_requires ]
        if missing_packages:
            print( f"Adding missing packages to install_requires: {missing_packages}" )
            self.install_requires.extend( missing_packages )
        else:
            print( "No packages to update." )
        return self.install_requires
    
    ## end class InstallRequiresHelper
    

## helpers end ------------------------------------------------------


## ok, let's get to work --------------------------------------------


## handle the commit hash -------------------------------------------
commit_hash: str = get_git_commit_hash()
with open('./commit_info.py', 'w') as f:
    f.write( f"COMMIT_HASH = '{commit_hash}'\n" )

## define initial install_requires list ----------------------------
initial_install_requires = [
    'columnar==1.4.1',
    'toolz==0.12.1',
    'wcwidth==0.2.13'
]

## create InstallRequiresHelper instance ----------------------------
helper = InstallRequiresHelper( './requirements_app/local.txt', initial_install_requires )

## build the real install_requires list if necessary ----------------
checked_install_requires: list = helper.update_install_requires_if_necessary()

## setup() ----------------------------------------------------------
setup(
    name='tools',
    version='1.1.1',
    description='Various BDR-related tools.',
    py_modules=['main', 'commit_info'],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['run_this=code_to_package.main:main'],
    },
    install_requires=checked_install_requires,
)
