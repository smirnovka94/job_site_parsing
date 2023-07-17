from abc import ABC, abstractmethod
import requests
from src.function import printj

class TOWN(ABC):
    @abstractmethod
    def get_id_town(self):
        pass

class SJ_city(TOWN):
    URL = 'https://api.superjob.ru/2.0/towns/geoip/'
    def __init__(self,  town):
        self.town = town
    def read_areas(self) -> list:
        '''Читаем данные из сайта: api.hh.ru/areas'
        :move: Чтение json
        :return: Список словарей
        '''
        response = requests.get(SJ_city.URL)
        data_json = response.json()
        return data_json

    def get_id_town(self):
        pass
        data = self.read_areas()
        # printj(json)
        for city in data['objects']:
            # pass
            if city["title"] == self.town:
                id_town = city['id']
                return id_town
class HH_city(TOWN):
    URL = 'https://api.hh.ru/areas'
    def __init__(self,  town):
        self.town = town
    def read_areas(self) -> list:
        '''Читаем данные из сайта: api.hh.ru/areas'
        :move: Чтение json
        :return: Список словарей
        '''
        response = requests.get(HH_city.URL)
        data_json = response.json()
        return data_json

    def get_id_town(self):
        data = self.read_areas()
        for d in data:
            from_countries = d['areas']
            for country in from_countries:
                if country['name'] == self.town:
                    id_town = country['id']
                    return id_town
                dict_towns = country["areas"]
                for dict_town in dict_towns:
                    if dict_town['name'] == self.town:
                        id_town = dict_town['id']
                        return id_town

class Vacancy():
    def __init__(self, data):
        self.id_s = data[0]
        self.name_s = data[1]
        self.city_s = data[2]
        self.url_s = data[3]
        self.salary_s = data[4]
        self.json = self.create_json()

    def create_json(self):
        for_json = []
        for i, item in enumerate(self.id_s):
            new_data = {
                "id": item,
                "name": self.name_s[i],
                "city": self.city_s[i],
                "url": self.url_s[i],
                "salary": self.salary_s[i]
            }
            for_json.append(new_data)
        return for_json

    def __add__(self, other):
        return self.json + other.json

class JSON_Vacancy(Vacancy):
    def __init__(self, data):
        self.id_s = [values['id'] for values in data]
        self.name_s = [values['name'] for values in data]
        self.city_s = [values['city'] for values in data]
        self.url_s = [values['url'] for values in data]
        self.salary_s = [values['salary'] for values in data]
        self.id_salary_dict = dict(zip(self.id_s, self.salary_s))

    def sort_vacancies_by_salary(self, data_dict ,a_b_c=True):
        """
        Сортировка по возрастанию ЗП(по умолчанию)
        :param a_b_c:
        :return:self.id_salary_dict
        """
        if data_dict == None:
            data_dict = self.id_salary_dict
        id_salary_dict = {k: v for k, v in sorted(data_dict.items(), key=lambda item: item[1], reverse=a_b_c)}
        return id_salary_dict

    def filter_salary(self, count):
        dict_filter = {}
        for k, v in self.id_salary_dict.items():
            if v >= count:
                dict_filter[k] = v
        return dict_filter

    def filter_without_salary(self):
        dict_filter = {}
        for k, v in self.id_salary_dict.items():
            if v == 0:
                dict_filter[k] = v
        return dict_filter