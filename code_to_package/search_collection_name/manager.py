"""
Manager module.
Calls utils.helper_function() if needed
"""

import json, logging
from .utils import grab_collection_info, prep_json_output, prep_text_output


log = logging.getLogger( __name__ )


def manage_processing( collection_name: str, collection_json_array_filepath: str, output_data_format: str ):
    """ Manages processing.
        Called by cli.run() with the parsed args. """
    log.debug( 'about to call helper-function' )
    # processed_data: str = helper_function( data )
    log.debug( f'collection_name, ``{collection_name}``' )
    log.debug( f'collection_json_array_filepath, ``{collection_json_array_filepath}``' )
    log.debug( f'output_data_format, ``{output_data_format}``' )
    if collection_name != None:
        data: dict = grab_collection_info( collection_name )
        if output_data_format == 'json':
            prepped_dct: dict = prep_json_output( data )
            output_json = json.dumps( prepped_dct, sort_keys=True, indent=2 )
            print( output_json )
        elif output_data_format == 'text':
            output_text: str = prep_text_output( collection_name, data )
            print( output_text )
    return
