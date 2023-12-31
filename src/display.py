import os
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from src.colors import *
from unidecode import unidecode

load_dotenv(find_dotenv())
FILENAME = os.environ.get("FILENAME")


def display():
    if os.path.exists(FILENAME):
        search_term = input(
            green
            + "\nPor favor ingrese si desea buscar por autor, título o por ISBN.\nSi no ingresa un valor, se mostrarán todas las entradas.\n\n"
            + reset
        )
        if search_term == "":
            df = pd.read_csv(FILENAME, encoding="utf-8")
            print(green, df, reset)
        elif search_term == "isbn" or search_term == "ISBN":
            isbn = input(
                green
                + "\nPor favor ingrese el ISBN del libro que desea consultar.\n\n"
                + reset
            )
            df = pd.read_csv(FILENAME, encoding="utf-8")
            condition = df["ISBN"] == int(isbn)
            df_filtered = df.loc[condition]
            print(green, df_filtered, reset)
        elif search_term == "autor" or search_term == "Autor":
            author = input(
                green
                + "\nPor favor ingrese el autor del libro que desea consultar.\n\n"
                + reset
            )
            df = pd.read_csv(FILENAME, encoding="utf-8")
            df_filtered = df.loc[
                df["Autor"]
                .str.normalize("NFKD")
                .str.encode("ascii", errors="ignore")
                .str.decode("utf-8")
                .str.lower()
                .str.contains(unidecode(author.lower()))
            ]
            print(green, df_filtered, reset)
        elif (
            search_term == "titulo"
            or search_term == "Titulo"
            or search_term == "Título"
            or search_term == "título"
        ):
            title = input(
                green
                + "\nPor favor ingrese el título del libro que desea consultar.\n\n"
                + reset
            )
            df = pd.read_csv(FILENAME, encoding="utf-8")
            df_filtered = df.loc[
                df["Título"]
                .str.normalize("NFKD")
                .str.encode("ascii", errors="ignore")
                .str.decode("utf-8")
                .str.lower()
                .str.contains(unidecode(title.lower()))
            ]
            print(green, df_filtered, reset)
    else:
        print(red, "\nNo hay datos para consultar.\n", reset)
