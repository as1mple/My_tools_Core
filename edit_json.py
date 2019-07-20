import json


def save(di: dict, arg= 'a+', path='save.json') -> None:
    with open(path, arg) as js:  # or 'w'
        js.write(json.dumps(di, indent=4) + ',\n')

def open_file(path: str) -> str:
    with open(path, 'r') as dataframe:
        return dataframe.readlines()
