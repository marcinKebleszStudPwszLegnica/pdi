from src.places import City, Street


class Cities(object):
    def __init__(self, file):
        self.file = file

    def find_by_id(self, city_id):
        with open(self.file, encoding="utf-8") as fp:
            lines = fp.readlines()
            city = self.__find_exact_city(lines, city_id)

            if not city:
                city = self.__find_fallback_city(lines, city_id)

            if city:
                return city

        return City("? (" + city_id + ")")

    @staticmethod
    def __find_exact_city(lines, city_id):
        for line in lines:
            if city_id + ";" + city_id in line:
                return City(line.split(";")[6])

    @staticmethod
    def __find_fallback_city(lines, city_id):
        for line in lines:
            if city_id in line:
                return City(line.split(";")[6])


class Streets(object):
    def __init__(self, file, cities):
        self.file = file
        self.cities = cities

    def find_by_street_name(self, street_name):
        with open(self.file, encoding="utf-8") as fp:
            lines = fp.readlines()
            for line in lines:
                if street_name.lower() in line.lower():
                    street = Street(line)
                    street.set_city(self.cities.find_by_id(street.city_id))
                    yield street

    def find_the_most_frequent_street_name_per_voivodeship(self, voivodeship):
        counts = dict()
        with open(self.file, encoding="utf-8") as fp:
            lines = fp.readlines()
            for line in lines:
                if len(line) > 1:
                    street = Street(line)
                    full_name = street.get_full_name()
                    if voivodeship == street.voivodeship_id:
                        if full_name in counts:
                            counts[full_name] += 1
                        else:
                            counts[full_name] = 1

        return sorted(counts.items(), key=lambda x: x[1], reverse=True)[0]

    def find_the_number_of_streets(self, street_name):
        counts = dict()
        with open(self.file, encoding="utf-8") as fp:
            lines = fp.readlines()
            for line in lines:
                if len(line) > 1:
                    street = Street(line)
                    if street_name.lower() in line.lower():
                        full_name = street.get_full_name()
                        if full_name in counts:
                            counts[full_name] += 1
                        else:
                            counts[full_name] = 1
        return counts

    def take_streets(self):
        counts = dict()
        with open("data/ULIC_Adresowy_2021-10-09.csv", encoding="utf-8") as fp:
            lines = fp.readlines()
            for line in lines:
                properties = line.split(';')
                if len(properties) == 10:
                    street_full_name = properties[7]
                    street_full_name = " ".join(street_full_name.split())
                    if street_full_name in counts:
                        counts[street_full_name] += 1
                    else:
                        counts[street_full_name] = 1

        return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:100]

    def find_the_same_street_name_per_city(self):
        counts = dict()
        with open(self.file, encoding="utf-8") as fp:
            lines = fp.readlines()
            for line in lines:
                properties = line.split(';')
                if len(properties) == 10:
                    street_full_name = properties[6] + " " + properties[8] + " " + properties[7]
                    street_full_name = " ".join(street_full_name.split())

                    street_name = properties[7]

                    for i in data:
                        if i['id_number'] == 'V410Z8':
                            print(i['birthdate'])
                            print(i['name'])
                            break

                    if street_name in counts:
                        counts[street_full_name] += 1
                    else:
                        counts[street_full_name] = 1

        return sorted(counts.items(), key=lambda x: x[1], reverse=True)[0]
