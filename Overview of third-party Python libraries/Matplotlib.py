# Библиотека matplotlib используется для визуализации данных в Python.

# Задача: Создать линейный график простой функции.


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = x ** 2

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot')
plt.show()