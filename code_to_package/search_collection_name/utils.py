import json, logging, pprint
import urllib.parse, urllib.request


log = logging.getLogger( __name__ )


def grab_collection_info( collection_name: str ) -> dict:
    """ Grabs pid and description for collection.
        Called by manager.manage_processing() 
        TODO: think about handling multiple results """
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


def prep_json_output( data ) -> dict:
    """ Prepares json output response.
        Called by manager.manage_processing() """
    ## grab parts ---------------------------------------------------
    params: dict = data['responseHeader']['params']
    collection_info: dict = data['response']['docs'][0]
    num_found = data['response']['numFound']
    pid = collection_info['pid']
    ## add view url -------------------------------------------------
    collection_info['view_url'] = f'https://repository.library.brown.edu/studio/collections/{pid}/'
    ## assemble parts and return ------------------------------------
    return_dct: dict = { 'params': params, 'collection_info': collection_info, 'num_found': num_found }
    log.debug( f'return_dct, ``{pprint.pformat(return_dct)}``' )
    return return_dct


def prep_text_output( collection_name: str, data: dict ) -> str:
    """ Prepares text output response.
        Called by manager.manage_processing() """
    ## grab parts ---------------------------------------------------
    pid: str = data['response']['docs'][0]['pid']
    description: str = data['response']['docs'][0]['collection_description_ssim'][0]
    view_url: str = f'https://repository.library.brown.edu/studio/collections/{pid}/'
    num_found: str = data['response']['numFound']
    ## assemble text and return -------------------------------------
    output_text = '-------\n'
    output_text += f'collection-name: \n{collection_name}\n\n'
    output_text += f'pid: \n{pid}\n\n'
    output_text += f'view_url: \n{view_url}\n\n'
    output_text += f'description: \n{description}\n\n'
    output_text += f'(num_found: {num_found})\n'
    output_text += '-------\n'
    log.debug( f'output_text, ``{output_text}``' )
    return output_text
