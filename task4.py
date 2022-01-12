# porównanie "popularności" miast, czyli wskazanie jakiej ulicy jest w kraju więcej
from src.cli import compare_two_streets
from src.repositories import Cities, Streets
from sys import argv

searched_streets = compare_two_streets(argv)

cities = Cities("data/SIMC_Urzedowy_2021-10-09.csv")
streets = Streets("data/ULIC_Adresowy_2021-10-09.csv", cities)

street_1 = streets.find_the_number_of_streets(searched_streets[1])
street_2 = streets.find_the_number_of_streets(searched_streets[2])
print(street_1)
print(street_2)

street_1_value = list(street_1.values())[0]
street_1_key = list(street_1.keys())[0]

street_2_value = list(street_2.values())[0]
street_2_key = list(street_2.keys())[0]

if street_1_value > street_2_value:
    print("Popularniejsza jest: " + street_1_key)
elif street_1_value < street_2_value:
    print("Popularniejsza jest: " + street_2_key)
else:
    print("Obie ulice są tak samo popularne")

# print(streets.take_streets())
