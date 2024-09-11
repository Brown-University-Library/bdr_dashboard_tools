"""
Manager module.
Calls utils.helper_function() if needed
"""

import logging
from .utils import helper_function


log = logging.getLogger( __name__ )


def manage_processing( collection_name: str, collection_json_array_filepath: str, output_data_format: str ):
    """ Manages processing.
        Called by cli.run() with the parsed args. """
    log.debug( 'about to call helper-function' )
    # processed_data: str = helper_function( data )
    log.debug( f'collection_name, ``{collection_name}``' )
    log.debug( f'collection_json_array_filepath, ``{collection_json_array_filepath}``' )
    log.debug( f'output_data_format, ``{output_data_format}``' )
    return




# def manage_processing( data: str ):
#     """ Manages processing.
#         Called by cli.run() with the parsed args. """
#     log.debug( 'about to call helper-function' )
#     processed_data: str = helper_function( data )
#     log.debug( f'back in manage_processing(); processed_data: ``{processed_data}``' )
    