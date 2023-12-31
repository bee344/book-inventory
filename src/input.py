import dateutil.parser as parser
from src.colors import *
import pandas as pd


def check_input(filename, isbn, request, entries):
    df = pd.read_csv(filename, encoding="utf-8").astype(object)
    hit = df["ISBN"].eq(int(isbn)).any()
    if hit == True:
        print(yellow, "\nActualizando libro.\n", isbn, reset)
        shelf = input(green + "\nPor favor ingrese el estante destino:\n" + reset)
        df.loc[df["ISBN"] == int(isbn), "Estante"] = shelf
        df["Autor"].str.replace(",", " - ", regex=True)
        df["Título"].str.replace(",", " - ", regex=True)
        df.to_csv("inventario.csv", sep=",", index=False, encoding="utf-8")
        return
    titles = ""
    for entry in range(0, entries):
        info = request["items"][entry - 1]["volumeInfo"]
        answer = input(
            cyan
            + "\n¿Este es el libro que busca? "
            + str(info["title"])
            + ": (s/n)\n"
            + reset
        )
        if answer == "n" or answer == "":
            continue
        else:
            titles = str(info["title"])
            if "authors" in info:
                answer = input(
                    cyan
                    + "\n¿Este es el autor correcto? "
                    + str(info["authors"][0])
                    + ": (s/n)\n"
                    + reset
                )
                if answer == "s":
                    authors = info["authors"][0]
                else:
                    authors = input(
                        green + "\nPor favor ingrese el autor correcto.\n" + reset
                    )
            else:
                authors = input(
                    red
                    + "\nNo se ha encontrado el autor. Por favor ingréselo: \n"
                    + reset
                )
            if "publisher" in info:
                answer = input(
                    cyan
                    + "\n¿Esta es la editorial correcta? "
                    + str(info["publisher"])
                    + ": (s/n)\n"
                    + reset
                )
                if answer == "s":
                    publishers = str(info["publisher"])
                else:
                    publishers = input(
                        green + "\nPor favor ingrese la editorial correcta.\n" + reset
                    )
                publishers = str(info["publisher"])
            else:
                publishers = input(
                    red
                    + "\nNo se ha encontrado información de la editorial. Por favor ingrese el nombre:\n"
                    + reset
                )
            if "publishedDate" in info:
                answer = input(
                    cyan
                    + "\n¿Este es el año de edición correcto? "
                    + str(parser.parse(info["publishedDate"]).year)
                    + ": (s/n)\n"
                    + reset
                )
                if answer == "s":
                    dates = str(parser.parse(info["publishedDate"]).year)
                else:
                    dates = input(
                        green
                        + "\nPor favor ingrese el año de publicación correcto.\n"
                        + reset
                    )
            else:
                dates = input(
                    red
                    + "\nNo se ha encontrado el año de publicación. Por favor ingréselo:\n"
                    + reset
                )
            new_row = [
                int(isbn),
                titles.title(),
                authors.title(),
                publishers.title(),
                dates,
            ]
            break
    if titles == "":
        new_row = ask_input(isbn)
    shelf = input(green + "\nPor favor ingrese el estante destino:\n" + reset)
    df.loc[len(df.index)] = [
        int(isbn),
        new_row[1],
        new_row[2],
        new_row[3],
        new_row[4],
        shelf,
    ]
    df["Autor"].str.replace(",", " - ", regex=True)
    df["Título"].str.replace(",", " - ", regex=True)
    df.to_csv("inventario.csv", sep=",", index=False, encoding="utf-8")


def ask_input(isbn):
    print(
        red,
        "\nNo se ha encontrado el libro, por favor ingrese los datos manualmente.",
        reset,
    )
    titles = input(green + "\nPor favor ingrese el título del libro:\n" + reset)
    authors = input(green + "\nPor favor ingrese el nombre del autor: \n" + reset)
    publishers = input(
        green + "\nPor favor ingrese el nombre de la editorial:\n" + reset
    )
    dates = input(green + "\nPor favor ingrese el año de publicación:\n" + reset)
    new_row = [int(isbn), titles.title(), authors.title(), publishers.title(), dates]
    return new_row
