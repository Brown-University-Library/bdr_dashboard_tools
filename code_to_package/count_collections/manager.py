"""
Manager module.
Calls utils.helper_function() if needed
"""

import json, logging, pprint
from columnar import columnar
from .utils import helper_function, get_bdr_collections


log = logging.getLogger( __name__ )


def manage_processing( data: str ):
    """ Manages processing.
        Code credit: <https://github.com/contrick64>
        Called by cli.run() with the parsed args. """
    ## get bdr top-collections data ---------------------------------
    bdr_collections: dict = get_bdr_collections()
    ## format output ------------------------------------------------
    if data == 'json':
        info_dict = { 
            'data': bdr_collections, 
            'info': 'Top 100 collections, by number of items.',  }
        data = json.dumps( info_dict, indent=2 )  # don't sort keys, keep the data in the order-by-count
        print( data )
    else:
        colls_table = [ [key,value] for key,value in bdr_collections.items() ]
        table_headers = [ 'collection','no. items' ]
        print( columnar(colls_table,headers=table_headers,no_borders=True) )
        print( f'Total number of collections: {len(bdr_collections)}' )    
