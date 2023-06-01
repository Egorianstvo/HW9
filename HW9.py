# -*- coding: utf-8 -*-
"""Home9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GCusVbTFGpio7jgJ0-VPIMOgUq5zHUkk

Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).
"""

import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')

print(df[(df['population'] > 0) & (df['population'] < 500)].median_house_value.mean())

"""Задача 42: Узнать какая максимальная households в зоне минимального значения population."""

print(df[df['population']==df['population'].min()].households.max())