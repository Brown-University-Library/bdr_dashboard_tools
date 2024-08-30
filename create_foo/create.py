from .utils import helper_function

def create( data: str ):
    print( f'in create_foo.create.create(); data: ``{data}``')
    processed_data = helper_function( data )
    print( f'back in create_foo.create.create(); processed_data: ``{processed_data}``' )