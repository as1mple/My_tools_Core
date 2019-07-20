import argparse


def pars() -> list:
    parse = argparse.ArgumentParser(description='Test')
    parse.add_argument('--variable1', type=str, default=0)
    parse.add_argument('--variable2', type=int, default=1)
    arg = parse.parse_args()

    return [arg.variable1, arg.variable2]
