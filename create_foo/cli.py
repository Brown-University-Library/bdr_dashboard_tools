"""
Parses and validates args.
Calls the manager function.
"""

import argparse
from .manager import manage_processing


def run( args: list ) -> None:
    print( 'in create_foo.cli.run(); preparing arg-parser' )
    parser = argparse.ArgumentParser(description="Create Foo Command")
    parser.add_argument('--data', required=True, help='Data to create foo with')
    parsed_args = parser.parse_args(args)
    data: str = parsed_args.data

    print( '...and about to call create_foo.manager.manage_processing()' )
    manage_processing( data )  # Pass the parsed data to the create function
    return