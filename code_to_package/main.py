import logging, os, pathlib, pprint, sys


## setup logging ----------------------------------------------------
LOGLEVEL: str = os.environ.get( 'UM__LOGLEVEL', 'INFO' )  # 'DEBUG' or 'INFO'
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
from code_to_package.update_foo import cli as update_cli


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        args: list = sys.argv[2:]  # Collect all the additional arguments after the command
        if command == 'count_collections':
            log.debug( 'in count_collections.main.main(); calling count_collections.cli.run()' )
            count_collections_cli.run(args)
        elif command == 'update_foo':
            log.debug( 'in update_foo.main.main(); calling update_foo.cli.run()' )
            update_cli.run(args)
        else:
            log.debug(f'Unknown command: `{command}`')
    else:
        log.debug('No command provided.')


if __name__ == '__main__':
    main()
