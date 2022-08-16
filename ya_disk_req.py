import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, Yadisk_path):
        basic_url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": Yadisk_path, "overwrite": "true"}
        response = requests.get(basic_url, headers=headers, params=params)
        upload_url = response.json().get('href', '')
        return upload_url

    def upload_file(self, path_to_file):
        upload_url = self.get_upload_link(os.path.basename(path_to_file))
        response = requests.put(upload_url, data=open(path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Файл загружен")


if __name__ == '__main__':
    token = ''
    uploader = YaUploader(token)
    path_to_file = os.path.join(os.getcwd(), 'netology_test.txt')

    uploader.upload_file(path_to_file)