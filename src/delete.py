import os
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from src.colors import *
from unidecode import unidecode

load_dotenv(find_dotenv())
FILENAME = os.environ.get("FILENAME")


def delete():
    if os.path.exists(FILENAME):
        author = input(
            green
            + "\nPor favor ingrese el autor del libro que desea eliminar.\nSi no ingresa un valor, se mostrarán todas las entradas.\n\n"
            + reset
        )
        if author == "":
            df = pd.read_csv(FILENAME, encoding="utf-8")
            print(green, df, reset)
        else:
            df = pd.read_csv(FILENAME, encoding="utf-8")
            df_filtered = df.loc[
                df["Autor"]
                .str.normalize("NFKD")
                .str.encode("ascii", errors="ignore")
                .str.decode("utf-8")
                .str.lower()
                .str.contains(unidecode(author.lower()))
            ]
            if df_filtered.empty:
                print(
                    green,
                    "\nNo se han encontrado valores para la consulta realizada, volviendo al menú principal\n",
                    reset,
                )
                return
            print(green, df_filtered, reset)
            title = input(
                green
                + "\nPor favor ingrese el título del libro que desea eliminar.\nSi no ingresa un valor, se eliminarán todas las entradas.\n\n"
                + reset
            )
            if title == "":
                confirmation = input(
                    red
                    + "\n¿Desea eliminar todas las entradas de este autor? (s/n)\n"
                    + reset
                )
                if (
                    confirmation == "n"
                    or confirmation == "no"
                    or confirmation == "No"
                    or confirmation == "N"
                ):
                    title = input(
                        green
                        + "\nPor favor ingrese el título del libro que desea eliminar.\nSi no ingresa un valor, se eliminarán todas las entradas.\n\n"
                        + reset
                    )
                    while title == "":
                        title = input(green + "\nDebe ingresar un título\n" + reset)
                    df_filtered = df_filtered.loc[
                        df["Título"]
                        .str.normalize("NFKD")
                        .str.encode("ascii", errors="ignore")
                        .str.decode("utf-8")
                        .str.lower()
                        .str.contains(unidecode(title.lower()))
                    ]
                    if df_filtered.empty:
                        print(
                            green,
                            "\nNo se han encontrado valores para la consulta realizada, volviendo al menú principal\n",
                            reset,
                        )
                        return
                    confirmation = input(
                        yellow
                        + "\nEstas son las filas que eliminará. ¿Es correcto?\n"
                        + reset
                    )
                    if (
                        confirmation == "s"
                        or confirmation == "si"
                        or confirmation == "sí"
                        or confirmation == "S"
                        or confirmation == "Sí"
                        or confirmation == "Si"
                    ):
                        index_to_drop = df_filtered.index
                        df.drop(index_to_drop, inplace=True)
                        print(green, "\nEsta es la nueva lista:\n", df, reset)
                        df.to_csv(
                            "inventario.csv", sep=",", index=False, encoding="utf-8"
                        )
                    else:
                        print("\nPor favor realice la selección nuevamente.\n")
                        delete()
                else:
                    index_to_drop = df_filtered.index
                    df.drop(index_to_drop, inplace=True)
                    print(green, "\nEsta es la nueva lista:\n", df, reset)
                    df.to_csv("inventario.csv", sep=",", index=False, encoding="utf-8")
            else:
                df_filtered = df_filtered.loc[
                    df["Título"]
                    .str.normalize("NFKD")
                    .str.encode("ascii", errors="ignore")
                    .str.decode("utf-8")
                    .str.lower()
                    .str.contains(unidecode(title.lower()))
                ]
                if df_filtered.empty:
                    print(
                        green,
                        "\nNo se han encontrado valores para la consulta realizada, volviendo al menú principal\n",
                        reset,
                    )
                    return
                print(green, "\nEsta es la fila que eliminará.\n", df_filtered, reset)
                confirmation = input(yellow + "\n¿Es correcto?\n" + reset)
                if (
                    confirmation == "s"
                    or confirmation == "si"
                    or confirmation == "sí"
                    or confirmation == "S"
                    or confirmation == "Sí"
                    or confirmation == "Si"
                ):
                    index_to_drop = df_filtered.index
                    df.drop(index_to_drop, inplace=True)
                    print(green, "\nEsta es la nueva lista:\n", df, reset)
                    df.to_csv("inventario.csv", sep=",", index=False, encoding="utf-8")
                else:
                    print("\nPor favor realice la selección nuevamente.\n")
                    delete()
