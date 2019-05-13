import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fileName = 'studentInfo.csv'
with open(fileName) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    age = []

    for row in reader:
     age.append(str(row[7]))

    print(age)
    plt.bar(age,height=100000)
    plt.show()
