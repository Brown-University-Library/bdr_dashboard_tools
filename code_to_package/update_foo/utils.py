import logging


log = logging.getLogger( __name__ )


def helper_function( data: str ) -> str:
    log.debug( 'in update_foo.utils.helper_function()' )
    data = data.upper()
    log.debug( f'...data is now: ``{data}``' )
    return data
