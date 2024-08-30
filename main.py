import sys
from .create_foo import cli as create_cli
from .update_foo import cli as update_cli

def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'create_foo':
            create_cli.run()
        elif command == 'update_foo':
            update_cli.run()
        else:
            print(f"Unknown command: {command}")
    else:
        print("No command provided.")

if __name__ == '__main__':
    main()
