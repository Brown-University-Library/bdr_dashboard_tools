"""
Parses and validates args.
Calls the manager function.
"""

import argparse, logging
from .manager import manage_processing


log = logging.getLogger( __name__ )


def run( args: list ) -> None:
    log.debug( 'in create_foo.cli.run(); preparing arg-parser' )
    parser = argparse.ArgumentParser( description="Create Foo Command" )
    parser.add_argument('--output', required=True, help='"json" or "columnar"')
    parsed_args = parser.parse_args(args)
    output_data_format: str = parsed_args.output
    log.debug( f'parsed_args.data, ``{output_data_format}``' )
    if output_data_format not in ['json', 'columnar']:
        msg = f'Invalid data format: `{output_data_format}`; output should be "json" or "columnar"' 
        raise ValueError( msg )
    log.debug( '...and about to call create_foo.manager.manage_processing()' )
    manage_processing( output_data_format )  # Pass the parsed data to the create function
    return