import json
import requests
from src.function import printj


class JSONSaver():
    def __init__(self, data):
        self.data = data
        self.file_name = "find_vacancy.json"

    def save_to_json(self):
        # Сохраняем данные вакансий в JSON файл
        with open(self.file_name, 'w') as filename:
            json.dump(self.data, filename, indent=4)

    def read_json(self):
        # Читаем данные вакансий в JSON файл
        with open(self.file_name, mode='r', encoding='utf-8') as file:
            read_data = json.load(file)
            return read_data