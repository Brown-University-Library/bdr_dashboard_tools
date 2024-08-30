from setuptools import setup, find_packages

setup(
    name='tools',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tools=tools.main:main',
        ],
    },
)
