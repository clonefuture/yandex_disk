import json
import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, path_to_file):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {'path': path_to_file, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        href = response.json().get('href', '')
        response = requests.put(href, data=open(path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = r'\Users\user\Documents\Python\Homework\read_write_file\sorted.txt'
    token = ''
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
