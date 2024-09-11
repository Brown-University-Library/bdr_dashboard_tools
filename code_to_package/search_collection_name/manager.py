"""
Manager module.
Calls utils.helper_function() if needed
"""

import logging
from .utils import helper_function


log = logging.getLogger( __name__ )


def manage_processing( data: str ):
    """ Manages processing.
        Called by cli.run() with the parsed args. """
    log.debug( 'about to call helper-function' )
    processed_data: str = helper_function( data )
    log.debug( f'back in manage_processing(); processed_data: ``{processed_data}``' )
    