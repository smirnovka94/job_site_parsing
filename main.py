
from src.classnames import Vacancy, JSON_Vacancy
from src.files import JSONSaver
from src.function import printj
from src.hh_vacancies import HeadHunterAPI
from src.superjob_vacancies import SuperJobAPI
from src.user import user_input, user_output, user_filter_sort_parameters

if __name__ == '__main__':

    #Ввод исходных данных
    search_query, filter_towns = user_input()
    while True:
        repit_result_seach = input("Изменить поиск с новыми условиями поиска? Да/Нет\n")
        repit_result_seach = repit_result_seach.title()
        if repit_result_seach == "Да":
            user_input()
        elif repit_result_seach == "Нет":
            break
        else:
            print("Введите корректный ответ")


    # Запускаем поиск в HH.ru
    hh_api = HeadHunterAPI(search_query)
    # Фильтруем поиск по городам
    hh_api.get_towns(filter_towns)
    # Получаем сокращенные данные по вакансиям из API сайта
    hh_vacancy = hh_api.short_data_vacancy()

    # Запускаем поиск в Suorejob.ru
    sj_api = SuperJobAPI(search_query)
    # фильтруем поиск по городам
    sj_api.get_towns(filter_towns)
    # Получаем сокращенные данные по вакансиям из API сайта
    sj_vacancy = sj_api.short_data_vacancy()

    vac1 = Vacancy(hh_vacancy)
    vac2 = Vacancy(sj_vacancy)
    vac = vac1 + vac2

    # Сохраняем найденные вакансии в файл JSON
    json_saver = JSONSaver(vac)
    json_saver.save_to_json()

    # Читаем файл JSON
    from_json = json_saver.read_json()
    save_vacancy = JSON_Vacancy(from_json)

    # Фильтруем и сортируем данные
    sort_vacancy = user_filter_sort_parameters(save_vacancy)

    # Выводим резильтат
    user_output(sort_vacancy, save_vacancy)


