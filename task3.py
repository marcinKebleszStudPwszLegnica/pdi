# porównanie "popularności" miast, czyli wskazanie jakiej ulicy jest w kraju więcej
from src.cli import compare_two_streets
from src.repositories import Cities, Streets
from sys import argv

searched_streets = compare_two_streets(argv)

cities = Cities("data/SIMC_Urzedowy_2021-10-09.csv")
streets = Streets("data/ULIC_Adresowy_2021-10-09.csv", cities)


 print(streets.take_streets())
