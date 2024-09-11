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
    parser = argparse.ArgumentParser( description='Parses search_collection_name arguments' )
    parser.add_argument( '--collection_name', required=False, help='collection name to search for' )
    parser.add_argument( '--collection_json_array_file', required=False, help='input.json file, of array of names, to load' )
    parser.add_argument( '--output', required=True, help='"json" or "columnar"' )
    parsed_args = parser.parse_args(args)
    ## validate output arg ------------------------------------------
    output_data_format: str = parsed_args.output
    if output_data_format not in ['json', 'columnar']:
        msg = f'Invalid data format: `{output_data_format}`; output should be "json" or "columnar"' 
        raise ValueError( msg )
    ## validate collection args -------------------------------------
    if parsed_args.collection_name and parsed_args.collection_json_array_file:
        msg = 'Only one of --collection_name or --collection_json_array_file should be provided'
        raise ValueError( msg )
    if not parsed_args.collection_name and not parsed_args.collection_json_array_file:
        msg = 'One of --collection_name or --collection_json_array_file should be provided'
        raise ValueError( msg )
    ## call manager function ----------------------------------------
    manage_processing( output_data_format )  # Pass the parsed data to the create function
    return
