"""
cli.py... 
- parses and validates the module-specific command-line arguments
- calls the module's manager-function with the parsed arguments
"""

import argparse, logging
from .manager import manage_processing


log = logging.getLogger( __name__ )


def run( args: list ) -> None:
    log.debug( 'preparing arg-parser' )
    parser = argparse.ArgumentParser(description="Update Foo Command")
    parser.add_argument('--output', required=True, help='Data to update foo with')
    parsed_args = parser.parse_args(args)
    output_data_format: str = parsed_args.output

    manage_processing( output_data_format )  # Pass the parsed data to the update function
    return
