import sys
from .create_foo import cli as create_cli
from .update_foo import cli as update_cli


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        args: list = sys.argv[2:]  # Collect all the additional arguments after the command
        if command == 'create_foo':
            print( 'in create_foo.main.main(); calling create_foo.cli.run()' )
            create_cli.run(args)
        elif command == 'update_foo':
            print( 'in update_foo.main.main(); calling update_foo.cli.run()' )
            update_cli.run(args)
        else:
            print(f'Unknown command: `{command}`')
    else:
        print('No command provided.')


if __name__ == '__main__':
    main()
