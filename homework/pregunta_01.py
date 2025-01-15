"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Vamos a quitar las primeras cuatro líneas
    data_lines = lines[4:]

    data_lines

    registros: list = []
    registro: dict = {}

    for line in data_lines:
        # Si la línea está vacía no la tenemos en cuenta
        if line.strip() == "":
            registro["principales_palabras_clave"] = (
                re.sub(r"\s{2,}", " ", registro["principales_palabras_clave"])
                .rstrip(".")
                .rstrip(" ")
            )

            registros.append(
                [
                    registro["cluster"],
                    registro["cantidad_de_palabras_clave"],
                    registro["porcentaje_de_palabras_clave"],
                    registro["principales_palabras_clave"],
                ]
            )

            registro = {}
            continue

        match = re.match(r"\s*(\d+)\s+(\d+)\s+([\d,]+)\s*%\s+(.*)", line)

        if match:
            cluster = int(match.group(1))  # Primer número
            cantidad_de_palabras_clave = int(match.group(2))  # Segundo número
            porcentaje_de_palabras_clave = float(
                match.group(3).replace(",", ".")
            )  # Tercer número (con coma reemplazada por punto)
            principales_palabras_clave = (
                match.group(4).lstrip().replace("\n", "").strip("'")
            )  # Cuarto grupo palabras clave

            registro["cluster"] = cluster
            registro["cantidad_de_palabras_clave"] = cantidad_de_palabras_clave
            registro["porcentaje_de_palabras_clave"] = porcentaje_de_palabras_clave

            if not principales_palabras_clave.endswith(" "):
                principales_palabras_clave += " "

            registro["principales_palabras_clave"] = principales_palabras_clave

            if not principales_palabras_clave.endswith(" "):
                principales_palabras_clave += " "

        else:
            match2 = re.match(r"\s*(.*)", line)

            principales_palabras_clave = match2.group(1).lstrip().replace("\n", "")

            if not principales_palabras_clave.endswith(
                "."
            ) and not principales_palabras_clave.endswith(" "):
                principales_palabras_clave += " "

            registro["principales_palabras_clave"] += principales_palabras_clave

    column_names = [
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave",
    ]

    df = pd.DataFrame(registros, columns=column_names)

    return df


if __name__ == "__main__":
    pregunta_01()
