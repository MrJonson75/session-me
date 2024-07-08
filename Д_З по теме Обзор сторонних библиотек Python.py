import json
from getpass import getpass
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt


import sys

import numpy as np
import requests
from PIL import Image, ImageDraw, ImageFont

from requests.auth import HTTPBasicAuth

"""             Пример работы с библиотекой Nampy эту задачу я решал на CodeWars"""
# Сумма пар
# При наличии списка целых чисел и единственного суммарного значения
# верните первые два значения в порядке их появления, которые в сумме образуют сумму.
#
# Если есть две или более пар с требуемой суммой,
# то решением является пара, второй элемент которой имеет наименьший индекс.

def sum_pairs(ints, s):
    ints = np.array(ints)
    for i in range(s):
        if list(*np.where(ints == i)) == []:
            ints = np.delete(ints, np.where(ints == s - i))
    pairs = [[ints.tolist()[i], ints.tolist()[j]] for i in range(len(ints.tolist()))
             for j in range(i + 1, len(ints.tolist())) if ints[i] + ints[j] == s]
    return pairs[[max(list(*np.where(ints == k[1])))
                  for k in pairs].index(min([max(list(*np.where(ints == k[1])))
                                             for k in pairs]))] if pairs != [] else None



l9 = [1] * 10000000
l9[len(l9) // 2 - 1] = 6
l9[len(l9) // 2] = 7
l9[len(l9) - 2] = 8
l9[len(l9) - 1] = -3
l9[0] = 13
l9[1] = 3

print(sum_pairs(l9, 13))
print(sum_pairs(l9, 5))
print(sum_pairs(l9,16))
print(sum_pairs(l9, 31))
print(sum_pairs([11, 3, 7, 5], 10))
print(sum_pairs([4, 3, 2, 3, 4], 6))
print(sum_pairs([0, 0, -2, 3], 2))
print(sum_pairs([10, 5, 2, 3, 7, 5], 10))


"""                 Пример использования библиотеки requests"""

response = requests.get('https://api.github.com')
response.encoding = 'utf-8'
res = response.json()

for key, value in res.items():
    print(f"{key}, --------> {value}")

with open("api_github.json", "w") as fp:
    json.dump(res, fp)


    """          Пример использования модуля pandas """


# Открываем файл для чтения
with open('api_github.json', 'r') as file:
    # Загружаем данные из файла
    data = json.load(file)

series_example = pd.Series(data)
print()
print(series_example)


"""                             Пример использования библиотеки matplotlib"""

vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]

plt.pie(vals, labels=labels, autopct='%1.1f%%')
plt.title("Распределение марок автомобилей на дороге")
plt.show()




"""                             Пример использования библиотеки Pillow """

url = 'https://i.artfile.ru/2048x1365_1291675_[www.ArtFile.ru].jpg'

try:
    resp = requests.get(url, stream=True).raw
except requests.exceptions.RequestException as e:
    sys.exit(1)

try:
    img = Image.open(resp)
except IOError:
    print("Не возможно открыть изображение")
    sys.exit(1)

idraw = ImageDraw.Draw(img)
text = "this image i downloaded from www.ArtFile.ru"

font = ImageFont.truetype("arial.ttf", size=80)

idraw.text((10, 10), text, font=font)

img.show()
img.save('sid.jpg', 'jpeg')



