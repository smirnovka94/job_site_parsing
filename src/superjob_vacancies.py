import os

import requests
import json

from src.classnames import API, SJ_city
from src.function import printj

class SuperJobAPI():
    def __init__(self, name):
        self.name = name

    def get_towns(self, towns: list):
        self.towns = towns

    @property
    def id_towns(self):
        pass
        id_cities = []
        for town in self.towns:
            city =  SJ_city(town)
            id_city = city.get_id_town()
            id_cities.append(id_city)
        return id_cities

    def get_vacancies(self):
        town_id = self.id_towns # Код региона
        vacancies_count = 3 # api запрещает запрашивать больше 100 вакансий
        params={
            'town': town_id,
            'count': vacancies_count,
            'keyword': self.name
        }

        headers = {'X-Api-App-Id' : "v3.r.137668704.a2b2f7c5d61d32cb5fb3c4bab5d78700a6c7a1c9.c538c10081adbb00c15fc717db28e56c18908629"}
        response = requests.get("https://api.superjob.ru/2.0/vacancies", params=params, headers=headers)
        return response.json()

    @property
    def id_s(self):
        id_s = [values['id'] for values in self.get_vacancies()["objects"]]
        return id_s
    @property
    def name_s(self):
        name_s = [values['profession'] for values in self.get_vacancies()["objects"]]
        return name_s
    @property
    def city_s(self):
        city_s = [values['town']['title'] for values in self.get_vacancies()["objects"]]
        return city_s
    @property
    def url_s(self):
        url_s = [values['link'] for values in self.get_vacancies()["objects"]]
        return url_s
    @property
    def salary_s(self):
        """
        Ищет указания Заработной платы
        :return: 0, при None
        :return: Зарплату 'до' , если Зарплата 'от' не указана
        :return: Зарплату 'от' , во всех остальных случаях
        """
        salary_s = []
        for values in self.get_vacancies()["objects"]:
            if values['payment_from'] == None:
                salary_s.append(0)
                continue
            elif values['payment_from'] == None:
                salary_s.append(int(values['payment_to']))
            else:
                salary_s.append(int(values['payment_from']))
        return salary_s
    def short_data_vacancy(self):
        return self.id_s, self.name_s, self.city_s, self.url_s, self.salary_s







#
# # Ваш ID и секретный ключ
# client_id = '2737'
# secret_key = 'v3.r.137668704.77c96d8172f5abfd22642ad5251a89a5739c6023.9e5c53ff088fbd65bcc547109dfe37be534b399b'
#
# # URL для получения данных о вакансиях
# url = f'https://api.superjob.ru/2.0/vacancies/?catalogues=48' \
#       f'town=4&' \
#       f'count=100&' \
#       f'show_agreement=1&' \
#       f'catalogues_required=1&' \
#       f'o_agreement=0&' \
#       f'need_experience=0&' \
#       f'has_test=0&' \
#       f'payment_period=1&' \
#       f'town_include_null=0&' \
#       f'page=5'
#
# # Заголовок с авторизационными данными (ваш ID и секретный ключ)
# headers = {
#     'X-Api-App-Id': client_id,
#     'X-Api-App-Secret': secret_key,
# }
#
# # Отправляем запрос и получаем ответ
# response = requests.get(url, headers=headers)
# data = response.json()
#
# print(data)


# Обратите внимание, что в примере использованы следующие параметры запроса:
#
# - catalogues: идентификаторы каталогов вакансий (48 - IT, интернет, связь, телекоммуникации)
# - town: идентификатор города (4 - Москва)
# - count: количество вакансий на странице (максимум 100)
# - show_agreement: показывать только трудовые договоры (1)
# - catalogues_required: только вакансии из указанных каталогов (1)
# - no_agreement: исключить вакансии без трудового договора (0)
# - need_experience: требуется ли опыт работы (0 - без опыта)
# - has_test: наличие теста (0 - без тестов)
# - payment_period: период выплаты ЗП (1 - почасовая)
