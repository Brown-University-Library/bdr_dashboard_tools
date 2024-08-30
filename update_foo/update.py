from .utils import helper_function

def update( data: str ):
    print( f'in update_foo.update.update(); data: ``{data}``')
    processed_data = helper_function( data )
    print( f'back in update_foo.update.update(); processed_data: ``{processed_data}``' )