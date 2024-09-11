import logging, json, pprint, urllib.request
# import urllib.request


log = logging.getLogger( __name__ )


def helper_function( data: str ) -> str:
    log.debug( 'in create_foo.utils.helper_function()' )
    data = data.upper()
    log.debug( f'...data is now: ``{data}``' )
    return data


def get_bdr_collections() -> dict:
    ''' Returns a dict like "'collection name':[number of items]"
        Called by count_collections.manager.manage_processing() '''
    collection_field = 'ir_collection_name' # field to facet on
    bdr_api = 'https://repository.library.brown.edu/api/search/'
    # solr_query = f'?q=*&facet=on&facet.field={collection_field}&rows=0'
    solr_query = f'?q=*&facet=on&facet.field={collection_field}&rows=0&fl=ir_collection_name,pid'
    log.debug( f'solr_query, ``{solr_query}``' )
    full_url = bdr_api + solr_query
    log.debug( f'full_url, ``{full_url}``' )

    # query_result = urllib.request.urlopen(bdr_api + solr_query).read()
    query_result = urllib.request.urlopen(full_url).read()
    qjson = json.loads(query_result)
    log.debug( f'qjson, ```{pprint.pformat(qjson)}```' )
    # drill down to list
    facet_counts = qjson['facet_counts']['facet_fields'][collection_field]
    
    # facet_counts is a list like: 
    #   ['collection name', # items,'collection name', # items, ...]
    # so, make dict like:
    #   {facet_counts[0]:facet_counts[1],facet_counts[2]:facet_counts[3], ...]
    facet_iter = iter(list(facet_counts))
    result = {i:next(facet_iter) for i in facet_iter}

    return result 
