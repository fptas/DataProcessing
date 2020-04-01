from pprint import pprint
import requests
import json

api_key = 'trnsl.1.1.20200401T183653Z.45c61c372bff67f1.308b98ed73e7cd0a7a52a88e99bb68234a49f9d4'

lang = 'ru-en'

texts = []
while True:
    str = input('Введите фразу для перевода RU->EN (или Enter для окончания ввода:)')
    if str == '' and len(texts) > 0:
        break
    if str > '':
        texts.append(str)
textstr = '&text='.join(texts)

full_link = f'https://translate.yandex.net/api/v1.5/tr.json/translate?key={api_key}&text={textstr}&lang={lang}'
response = requests.get(full_link)
with open('response.json', 'w') as file:
    file.write(response.text)

data = json.loads(response.text)
print(data)
responses = data["text"]

print('\nПереводы фраз:')
for i in range(len(texts)):
    print(f'{texts[i]} ==> {responses[i]}')



