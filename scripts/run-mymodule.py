import sys
import click

sys.path.append('.')
sys.path.append('modules/mymodule')

from modules.mymodule.src.core import check_folder

@click.command()
@click.argument('path')
@click.help_option('-h', '--help')
def main(path:str):
    check_folder(path)

if __name__ == '__main__':
    main()