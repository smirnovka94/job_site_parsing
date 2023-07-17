from src.classnames import HH_city
from src.function import input_filter_towns
from src.hh_vacancies import HeadHunterAPI
from src.superjob_vacancies import SuperJobAPI


def user_input():
    search_query = input("Введите Вакансию для поиска: ")
    #Создается большой JSON с вакансиями

    #Ввводим корректно Города
    while True:
        filter_towns = input_filter_towns()
        if filter_towns == False:
            pass
        else: break

    return search_query, filter_towns

def user_filter_sort_parameters(data):
    # Вводим минимальную ЗП
    while True:
        filter_costs = input("Введите минимальную заработную плату\n")
        if filter_costs == '':
            filter_costs = 0
        try:
            filter_costs = float(filter_costs)
            break
        except ValueError:
            print("Введите числовое значение, или оставьте поле пустым")
    filter_sort_data = data.filter_salary(filter_costs)

    while True:
        without_salary = input("Показать вакансии без указаной заработной платы? Да/Нет\n")
        without_salary = without_salary.title()
        if without_salary == "Нет":
            break
        else:
            strip_salary = data.filter_without_salary()
            for k, v in strip_salary.items():
                filter_sort_data[str(k)] = int(v)
            break

    while True:
        a_b_c = input("Отображать вакансии с возрастанием Заработной платы? Да/Нет\n")
        if a_b_c == "Нет":
            filter_sort_data = data.sort_vacancies_by_salary(filter_sort_data)
            break
        else:
            filter_sort_data = data.sort_vacancies_by_salary(filter_sort_data, False)
            break
    return filter_sort_data

def user_output(sort_vacancy, json_vacancy):
    if sort_vacancy == "":
        print("Нет вакансий, соответствующих заданным критериям")
    else:
        for i, item in enumerate(sort_vacancy):
            sort_index = item  # ID Вакансии
            json_index = json_vacancy.id_s.index(sort_index)  # Позиция ID из JSON файла
            print(f"ID vacancy: {json_vacancy.id_s[json_index]}")
            print(f"Profession: {json_vacancy.name_s[json_index]}")
            print(f"URL: {json_vacancy.url_s[json_index]}")
            if json_vacancy.salary_s[json_index] == 0:
                print("Зарплата не указана\n")
            else:
                print(f"Зарплата: {json_vacancy.salary_s[json_index]} \n")
            if i < len(sort_vacancy)-1:
                exit = input("Показать следующую вакансию?\n"
                             "Enter - продолжить просмотр\n"
                             "Нет - завершить работу\n")
                exit = exit.title()
                if exit == "Нет":
                    break
                else:
                    continue
            break
    print("Вы просмотрели все найденные вакансии")