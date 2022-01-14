from src.cli import get_searched_phrase, get_mapbox
from src.repositories import Cities, Streets
from sys import argv

searched_street = get_searched_phrase(argv)

cities = Cities("data/SIMC_Urzedowy_2021-10-09.csv")
streets = Streets("data/ULIC_Adresowy_2021-10-09.csv", cities)

counter = 0
found_streets = streets.find_by_street_name(searched_street)

for street in found_streets:
    phrase = str(street.city) + ": " + street.get_full_name()
    print(phrase)
    counter = counter + 1

print(str(counter) + " streets were found.")
