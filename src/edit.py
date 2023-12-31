from src.info import *
from src.input import *
from dotenv import load_dotenv, find_dotenv
import os
from ast import literal_eval

load_dotenv(find_dotenv())
FILENAME = os.environ.get("FILENAME")
FIELDS = literal_eval(os.environ.get("FIELDS"))


def edit():
    df = pd.read_csv(FILENAME, encoding="utf-8").astype("object")
    answer = input(
        green
        + "\nPor favor ingrese si desea buscar por ISBN, autor o título:\n"
        + reset
    ).lower()
    if answer == "isbn":
        isbn = input(green + "\nPor favor ingrese el código ISBN del libro:\n" + reset)
        df_filtered = df.loc[
            df["ISBN"]
            .astype(str)
            .str.normalize("NFKD")
            .str.encode("ascii", errors="ignore")
            .str.decode("utf-8")
            .str.lower()
            .str.contains(str(isbn))
        ]
        if df_filtered.empty:
            print(
                green,
                "\nNo se han encontrado valores para la consulta realizada, volviendo al menú principal\n",
                reset,
            )
            return
        column = input(
            green
            + "\nPor favor ingrese qué columna desea editar (Título, Autor, Editorial, Edición o Estante):\n"
            + reset
        ).title()
        if column == "Edicion":
            column = "Edición"
        elif column == "Titulo":
            column = "Título"
        value = input(green + "\nPor favor ingrese el nuevo valor:\n" + reset)
        df.loc[
            df["ISBN"]
            .astype(str)
            .str.normalize("NFKD")
            .str.encode("ascii", errors="ignore")
            .str.decode("utf-8")
            .str.lower()
            .str.contains(str(isbn)),
            column,
        ] = value
        print(
            green,
            df.loc[
                df["ISBN"]
                .str.normalize("NFKD")
                .str.encode("ascii", errors="ignore")
                .str.decode("utf-8")
                .str.lower()
                .str.contains(str(isbn))
            ],
            reset,
        )
        df.to_csv("inventario.csv", sep=",", index=False, encoding="utf-8")
    elif answer == "título" or answer == "titulo":
        title = input(green + "\nPor favor ingrese el título del libro:\n" + reset)
        df_filtered = df.loc[
            df["Título"]
            .str.normalize("NFKD")
            .str.encode("ascii", errors="ignore")
            .str.decode("utf-8")
            .str.lower()
            .str.contains(title)
        ]
        if df_filtered.empty:
            print(
                green,
                "\nNo se han encontrado valores para la consulta realizada, volviendo al menú principal\n",
                reset,
            )
            return
        column = input(
            green
            + "\nPor favor ingrese qué columna desea editar (Título, Autor, Editorial, Edición o Estante):\n"
            + reset
        ).title()
        if column == "Edicion":
            column = "Edición"
        elif column == "Titulo":
            column = "Título"
        value = input(green + "\nPor favor ingrese el nuevo valor:\n" + reset)
        df.loc[
            df["Título"]
            .str.normalize("NFKD")
            .str.encode("ascii", errors="ignore")
            .str.decode("utf-8")
            .str.lower()
            .str.contains(title),
            column,
        ] = value
        print(
            green,
            df.loc[
                df["Título"]
                .str.normalize("NFKD")
                .str.encode("ascii", errors="ignore")
                .str.decode("utf-8")
                .str.lower()
                .str.contains(title)
            ],
            reset,
        )
        df.to_csv("inventario.csv", sep=",", index=False, encoding="utf-8")
    elif answer == "autor":
        author = input(green + "\nPor favor ingrese el autor del libro:\n" + reset)
        df_filtered = df.loc[
            df["Autor"]
            .str.normalize("NFKD")
            .str.encode("ascii", errors="ignore")
            .str.decode("utf-8")
            .str.lower()
            .str.contains(author)
        ]
        if df_filtered.empty:
            print(
                green,
                "\nNo se han encontrado valores para la consulta realizada, volviendo al menú principal\n",
                reset,
            )
            return
        column = input(
            green
            + "\nPor favor ingrese qué columna desea editar (Título, Autor, Editorial, Edición o Estante):\n"
            + reset
        ).title()
        if column == "Edicion":
            column = "Edición"
        elif column == "Titulo":
            column = "Título"
        value = input(green + "\nPor favor ingrese el nuevo valor:\n" + reset)
        df.loc[
            df["Autor"]
            .str.normalize("NFKD")
            .str.encode("ascii", errors="ignore")
            .str.decode("utf-8")
            .str.lower()
            .str.contains(author),
            column,
        ] = value
        print(
            green,
            df.loc[
                df["Autor"]
                .str.normalize("NFKD")
                .str.encode("ascii", errors="ignore")
                .str.decode("utf-8")
                .str.lower()
                .str.contains(author)
            ],
            reset,
        )
        df.to_csv("inventario.csv", sep=",", index=False, encoding="utf-8")
