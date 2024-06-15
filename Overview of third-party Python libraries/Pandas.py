
# Библиотека pandas используется для обработки и анализа данных в Python.

# Задача: Считывать данные из CSV-файла, выполнять простой анализ данных и распечатывать результаты

# CSV-файла взят рандомный из интернета.

import pandas as pd

data = pd.read_csv('data.csv')

print(data.head())
print(data.describe())