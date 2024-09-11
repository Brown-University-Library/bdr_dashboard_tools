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
    parser = argparse.ArgumentParser( description='Parses count_collections arguments' )
    parser.add_argument('--output', required=True, help='"json" or "columnar"')
    parsed_args = parser.parse_args(args)
    output_data_format: str = parsed_args.output
    log.debug( f'parsed_args.data, ``{output_data_format}``' )
    if output_data_format not in ['json', 'columnar']:
        msg = f'Invalid data format: `{output_data_format}`; output should be "json" or "columnar"' 
        raise ValueError( msg )
    manage_processing( output_data_format )  # Pass the parsed data to the create function
    return