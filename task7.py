from src.repositories import Cities, Streets

cities = Cities("data/SIMC_Urzedowy_2021-10-09.csv")
streets = Streets("data/ULIC_Adresowy_2021-10-09.csv", cities)

streets.find_the_city_with_the_most_streets()
