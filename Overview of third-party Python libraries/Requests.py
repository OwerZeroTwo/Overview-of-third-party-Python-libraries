# Библиотека requests используется для создания HTTP-запросов в Python.

# Задача: Получить данные из JSON API и распечатать их на консоли.




import requests
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = response.json()

print(data)
