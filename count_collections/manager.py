"""
Manager module.
Calls utils.helper_function() if needed
"""

from .utils import helper_function, get_bdr_collections

def manage_processing( data: str ):
    print( f'in create_foo.manage.manage_processing(); data: ``{data}``')
    # processed_data = helper_function( data )
    processed_data = get_bdr_collections()
    print( f'back in create_foo.manage.manage_processing(); processed_data: ``{processed_data}``' )