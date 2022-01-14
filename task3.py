# znajdowanie najpopularniejszej nazwy ulicy per województwo
from src.repositories import Cities, Streets

voivodeship = {
    'DOLNOŚLĄSKIE': '02',
    'KUJAWSKO-POMORSKIE': '04',
    'LUBELSKIE': '06',
    'LUBUSKIE': '08',
    'ŁÓDZKIE': '10',
    'MAŁOPOLSKIE': '12',
    'MAZOWIECKIE': '14',
    'OPOLSKIE': '16',
    'PODKARPACKIE': '18',
    'PODLASKIE': '20',
    'POMORSKIE': '22',
    'ŚLĄSKIE': '24',
    'ŚWIĘTOKRZYSKIE': '26',
    'WARMIŃSKO-MAZURSKIE': '28',
    'WIELKOPOLSKIE': '30',
    'ZACHODNIOPOMORSKIE': '32',
}

cities = Cities("data/SIMC_Urzedowy_2021-10-09.csv")
streets = Streets("data/ULIC_Adresowy_2021-10-09.csv", cities)


for voivodeship_name, voivodeship_id in voivodeship.items():
    street = streets.find_the_most_frequent_street_name_per_voivodeship(voivodeship_id)
    print(voivodeship_name + ": " + str(street))
