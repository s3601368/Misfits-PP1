
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#opens csv files , prints top 5 entries and returns the dataframe of the csv
def csv_preview(csv_name, len):
    studentVle = pd.read_csv(csv_name)
    print(studentVle.head(len))
    return studentVle

def sort_by_demographics(df, demographic):

    for demographics_results in df.groupby(['code_module', 'code_presentation']):
        sns.distplot(demographics_results[1].total_mark, bins=100, kde_kws={"label": "Everyone"})
        for i in df[demographic].unique():
            sns.distplot(demographics_results[1][demographics_results[1].age_band == i].total_mark, bins = 100, kde_kws={"label": i})

        plt.show()