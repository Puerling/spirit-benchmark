import re


def get_soliton(name: str):
    soliton = re.search(r"(hopfion|skyrmion)", name).group(1)
    return soliton
