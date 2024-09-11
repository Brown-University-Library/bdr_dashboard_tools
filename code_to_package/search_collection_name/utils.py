import json, logging, pprint
import urllib.parse, urllib.request


log = logging.getLogger( __name__ )


def grab_collection_info( collection_name: str ) -> dict:
    """ Grabs pid and description for collection.
        Called by manager.manage_processing() """
    log.debug( f'collection_name, ``{collection_name}``' )
    ## prep url -----------------------------------------------------
    api_url_root = 'https://repository.library.brown.edu/api/search/'
    params = { 
        'q': f'collection_name_ssim:"{collection_name}"',
        'rows': '25',
        'fl': 'pid,collection_description_ssim' 
        }
    query_string = urllib.parse.urlencode( params )
    full_url = f'{api_url_root}?{query_string}'
    ## make request -------------------------------------------------
    query_result: str = urllib.request.urlopen(full_url).read()
    ## process and return data --------------------------------------
    jsn_dct: dict = json.loads( query_result )
    log.debug( f'jsn_dct, ```{pprint.pformat(jsn_dct)}```' )
    return jsn_dct
