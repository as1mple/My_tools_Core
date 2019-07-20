import csv

import pandas as pd
from pandas import DataFrame


def read_csv(path: str) -> list:
    with open(path, 'r') as myFile:
        dataFromFile = csv.reader(myFile)
        data = (list(dataFromFile))
    return data


def read_csv_pandos(path: str) -> DataFrame:
    data = pd.read_csv(path)
    return data

