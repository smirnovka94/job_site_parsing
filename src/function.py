import json

#ДЛЯ ЧТЕНИЯ API ЗАПРОСОВ
def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

#ФУНККЦИИ ОБРАБОТКИ ВООДИМОЙ ИНФОРМАЦИИ
def find_isdigit(word):
    for w in word:
        if w.isdigit():
            print("В названии города не должно быть цифр")
            return True


def input_filter_towns():
    """
    Функция ввода и проверки на корректность списка городов
    """
    towns = []
    filter_towns = input("Введите список городов для сортировки, через запятую\n").split()
    for i, item in enumerate (filter_towns):
        if find_isdigit(item):
            return False
        else:
            towns.append(item.title())
    return towns