import cmd
from src.info import *
from src.input import *
from src.display import *
from src.add import *
from src.delete import *
from src.edit import *
from src.colors import *
from dotenv import load_dotenv, find_dotenv
import pyfiglet
from sys import exit

os.system("")

load_dotenv(find_dotenv())

title = pyfiglet.figlet_format(
    "Super Inventarius X Ultimate\n", width=60, font="slant", justify="center"
)


class Shell(cmd.Cmd):
    intro = (
        "\n"
        + title
        + "\nBienvenido a la interfaz del gestor de inventario.\n\
        \nEscriba ayuda o ? para ver las opciones.\n"
    )
    prompt = yellow + ">> " + reset
    file = None

    def do_ayuda(self, _args):
        "\nMuestra información sobre los comandos\n"
        return cmd.Cmd.do_help(self, _args)

    def do_agregar(self, _args):
        "\nAgrega o actualiza información al inventario\n"
        add()

    def do_mostrar(self, _args):
        "\nExhibir información de un libro o de todos los libros\n"
        display()

    def do_eliminar(self, _args):
        "\nEliminar libros del inventario\n"
        delete()

    def do_editar(self, _args):
        "\nEditar información de los libros del inventario\n"
        edit()

    def do_salir(self, _args):
        "\nSalir de la la aplicación\n"
        exit(yellow + "\nSaliendo de la aplicación.\nGracias por utilizarnos\n" + reset)


if __name__ == "__main__":
    Shell().cmdloop()
