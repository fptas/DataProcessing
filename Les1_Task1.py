from pprint import pprint
import requests
import json



main_link = 'https://api.github.com/users/'
command = 'repos'

username = input('Введите имя пользователя:')
full_link = f'{main_link}{username}/{command}'

#header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

response = requests.get(full_link)
data = json.loads(response.text)
if len(data) > 0:
    print(f'\nСписок репозиториев для пользователя {username}:')
    for i in data:
        print(i["name"])
else:
    print(f'\nУ пользователя {username} нет репозиториев.')


