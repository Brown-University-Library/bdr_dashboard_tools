import logging, os, pathlib, pprint, sys


## setup logging ----------------------------------------------------
LOGLEVEL: str = os.environ.get( 'BDT__LOGLEVEL', 'INFO' )  # 'DEBUG' or 'INFO' (namespacing for "BDR Dashboard Tools")
lglvldct = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO }
logging.basicConfig(
    level=lglvldct[LOGLEVEL],  # assigns the level-object to the level-key loaded from the envar
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S' )
log = logging.getLogger( __name__ )


## add the project directory to the sys.path
parent_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(parent_dir.parent) )
log.debug( f'sys-path:, ``{pprint.pformat(sys.path)}``' )

from code_to_package.count_collections import cli as count_collections_cli
from code_to_package.search_collection_name import cli as search_collection_name_cli


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        args: list = sys.argv[2:]  # Collect all the additional arguments after the command
        if command == 'count_collections':
            log.debug( 'calling count_collections.cli.run()' )
            count_collections_cli.run(args)
        elif command == 'search_collection_name':
            log.debug( 'calling search_collection_name_cli.run()' )
            search_collection_name_cli.run(args)
        else:
            print(f'Unknown command: `{command}`')
    else:
        print('No command provided.')


if __name__ == '__main__':
    main()
