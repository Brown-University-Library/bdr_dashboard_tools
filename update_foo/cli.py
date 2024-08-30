import argparse
from .update import update

def run( args: list ) -> None:
    print( 'in update_foo.cli.run(); preparing arg-parser' )
    parser = argparse.ArgumentParser(description="Update Foo Command")
    parser.add_argument('--data', required=True, help='Data to update foo with')
    parsed_args = parser.parse_args(args)
    data: str = parsed_args.data

    print( '...and about to call update_foo.upddate.update()' )
    update( data )  # Pass the parsed data to the update function
    return