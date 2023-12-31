from src.info import *
from src.input import *
from dotenv import load_dotenv, find_dotenv
import dateutil.parser as parser
import os
from ast import literal_eval

load_dotenv(find_dotenv())
FILENAME = os.environ.get("FILENAME")
FIELDS = literal_eval(os.environ.get("FIELDS"))


def add():
    isbn = input(green + "\nPor favor ingrese el código ISBN del libro:\n" + reset)
    r = make_request(isbn)
    if r["totalItems"] > 0:
        entries = len(r["items"])
        if os.path.exists(FILENAME):
            check_input(FILENAME, isbn, r, entries)
        else:
            for entry in range(0, entries):
                titles = ""
                info = r["items"][entry - 1]["volumeInfo"]
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
                                green
                                + "\nPor favor ingrese el autor correcto.\n"
                                + reset
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
                                green
                                + "\nPor favor ingrese la editorial correcta.\n"
                                + reset
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
                        str(authors).title(),
                        publishers.title(),
                        dates,
                    ]
                    break
            if titles == "":
                new_row = ask_input(isbn)
            shelf = input(green + "\nPor favor ingrese el estante destino:\n" + reset)
            my_dict = {
                "ISBN": [int(isbn)],
                "Título": [new_row[1]],
                "Autor": [new_row[2]],
                "Editorial": [new_row[3]],
                "Edición": [new_row[4]],
                "Estante": [shelf],
            }
            df = pd.DataFrame.from_dict(my_dict)
            df.to_csv("inventario.csv", sep=",", index=False, encoding="utf-8")
    else:
        if os.path.exists(FILENAME):
            df = pd.read_csv(FILENAME, encoding="utf-8").astype("object")
            hit = df["ISBN"].eq(float(isbn)).any()
            if hit == True:
                print(yellow, "\nActualizando libro.\n", isbn, reset)
                shelf = input(
                    green + "\nPor favor ingrese el estante destino:\n" + reset
                )
                df.loc[df["ISBN"] == int(isbn), "Estante"] = shelf
                return
            new_row = ask_input(isbn)
            shelf = input(green + "\nPor favor ingrese el estante destino:\n" + reset)
            df.loc[len(df.index)] = [
                isbn,
                new_row[1],
                new_row[2],
                new_row[3],
                new_row[4],
                shelf,
            ]
            df.to_csv("inventario.csv", sep=",", index=False, encoding="utf-8")
        else:
            new_row = ask_input(isbn)
            shelf = input(green + "\nPor favor ingrese el estante destino:\n" + reset)
            my_dict = {
                "ISBN": [int(isbn)],
                "Título": [new_row[1]],
                "Autor": [new_row[2]],
                "Editorial": [new_row[3]],
                "Edición": [new_row[4]],
                "Estante": [shelf],
            }
            df = pd.DataFrame.from_dict(my_dict)
            df.to_csv("inventario.csv", sep=",", index=False, encoding="utf-8")
