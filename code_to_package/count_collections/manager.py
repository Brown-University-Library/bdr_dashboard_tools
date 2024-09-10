"""
Manager module.
Calls utils.helper_function() if needed
"""

import logging
from columnar import columnar
from .utils import helper_function, get_bdr_collections


log = logging.getLogger( __name__ )


def manage_processing( data: str ):
    log.debug( f'in create_foo.manage.manage_processing(); data: ``{data}``')
    bdr_collections: dict = get_bdr_collections()

    colls_table = [[key,value] for key,value in bdr_collections.items()]
    table_headers = ['collection','no. items']
    log.debug(columnar(colls_table,headers=table_headers,no_borders=True))
    log.debug(f'Total number of collections: {len(bdr_collections)}')    
