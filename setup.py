# from setuptools import setup, find_packages

import subprocess
from setuptools import setup

def get_git_commit_hash() -> str:
    try:
        commit_hash = subprocess.check_output( ['git', 'rev-parse', 'HEAD'] ).strip().decode( 'utf-8' )
        return commit_hash
    except Exception as e:
        msg = f'Error obtaining git commit hash: {e}'
        raise Exception( msg )

commit_hash: str = get_git_commit_hash()
with open('./commit_info.py', 'w') as f:
    f.write( f"COMMIT_HASH = '{commit_hash}'\n" )

setup(
    name='tools',
    version='1.1.1',
    description='Various BDR-related tools.',
    py_modules=['main', 'commit_info'],
    entry_points={
        'console_scripts': ['run_this=main:main'],
    },
    ## eventually load this from base.txt
    install_requires=[
        'columnar==1.4.1',
        'toolz==0.12.1',
        'wcwidth==0.2.13'
        ],
)

# setup(
#     name='tools',
#     version='0.1',
#     packages=find_packages(),
#     entry_points={
#         'console_scripts': [
#             'tools=tools.main:main',
#         ],
#     },
# )
