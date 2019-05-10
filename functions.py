
import pandas as pd


#opens csv files , prints top 5 entries and returns the dataframe of the csv
def csv_preview(csv_name):
    studentVle = pd.read_csv(csv_name)
    print(studentVle.head())
    return studentVle
