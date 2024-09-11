import logging
from .utils import helper_function


log = logging.getLogger( __name__ )


def update( data: str ):
    log.debug( f'in update_foo.update.update(); data: ``{data}``')
    processed_data = helper_function( data )
    log.debug( f'back in update_foo.update.update(); processed_data: ``{processed_data}``' )
    