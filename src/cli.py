from src.map import Map


def get_searched_phrase(argv):
    if len(argv) < 2:
        exit("Try to pass argument: python3 task1.py Legnicka")

    return argv[1]


def compare_two_streets(argv):
    if len(argv) < 3:
        exit("Try to pass arguments: python3 task4.py Legnicka Wałbrzyska")

    return argv


def get_mapbox(argv):
    if len(argv) == 3:
        return Map(argv[2])

    return None
