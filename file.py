# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:57:01 2019

@author: richardg71
"""
import csv

with open('C:\\users\\richardg71\\Documents\\example.txt') as file:
    readCSV = csv.reader(file, delimiter=',')
    for row in readCSV:
        print(row)