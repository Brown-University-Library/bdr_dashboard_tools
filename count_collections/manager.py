"""
Manager module.
Calls utils.helper_function() if needed
"""

from columnar import columnar
from .utils import helper_function, get_bdr_collections

def manage_processing( data: str ):
    print( f'in create_foo.manage.manage_processing(); data: ``{data}``')
    # processed_data = helper_function( data )
    bdr_collections: dict = get_bdr_collections()

    colls_table = [[key,value] for key,value in bdr_collections.items()]
    table_headers = ['collection','no. items']
    print(columnar(colls_table,headers=table_headers,no_borders=True))
    print(f'Total number of collections: {len(bdr_collections)}')    
    # print( f'back in create_foo.manage.manage_processing(); processed_data: ``{processed_data}``' )