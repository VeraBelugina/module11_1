import requests

req = requests.get('https://requests.readthedocs.io/en/latest/')

print(req.encoding) # кодировка страницы
print(req.status_code) # код состояния запроса
print(req.elapsed) # время между отправкой запроса и возвратом ответа
print(req.url) # окончательный url ответа
print(req.headers) # словарь заголовков ответов, нечувствительный к регистру
print(req.ok) # True при удачном соединении, False при неудачном

req1 = requests.options('https://requests.readthedocs.io/en/latest/')

print(req1.headers['Allow'])
