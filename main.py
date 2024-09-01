import pathlib, pprint, sys

## add the project directory to the sys.path
parent_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(parent_dir.parent) )
print( f'sys-path:, ``{pprint.pformat(sys.path)}``' )

from tools.count_collections import cli as count_collections_cli
from tools.update_foo import cli as update_cli


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        args: list = sys.argv[2:]  # Collect all the additional arguments after the command
        if command == 'count_collections':
            print( 'in count_collections.main.main(); calling count_collections.cli.run()' )
            count_collections_cli.run(args)
        elif command == 'update_foo':
            print( 'in update_foo.main.main(); calling update_foo.cli.run()' )
            update_cli.run(args)
        else:
            print(f'Unknown command: `{command}`')
    else:
        print('No command provided.')


if __name__ == '__main__':
    main()
