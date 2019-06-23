
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import numpy as np
import os


# opens csv files , prints top x entries and returns the dataframe of the csv
def csv_preview(csv_name, x):
    student_vle = pd.read_csv(csv_name)
    print(student_vle.head(x))
    return student_vle


def plot_demographic_amounts(df, demographic):
    for demographics_results in df.groupby(['code_module', 'code_presentation']):
        print(demographics_results[0])

        my_path = '/home/marcy/PycharmProjects/MISFITS/'
        os.mkdir(my_path + str(demographics_results[0]) + '/')
        my_path = my_path + str(demographics_results[0]) + '/'
        for i in demographic:
            sns.countplot(x=i, data=demographics_results[1])
            my_file = str(demographics_results[0]) + '_' + i + '.png'
            plt.title("Bar Graph of " + i + " for module: " + str(demographics_results[0][0]) +
                      " and code presentation: " + str(demographics_results[0][1]))
            plt.savefig(os.path.join(my_path, my_file))
            plt.close()

def sort_by_demographics(df, demographic):

    for demographics_results in df.groupby(['code_module', 'code_presentation']):
        try:

            print(demographics_results[0][1])
            plt.title("Distribution of clicks for module: " + str(demographics_results[0][0]) +
                      " and code presentation: " + str(demographics_results[0][1]))
            try:
                everyone = sns.distplot(
                    demographics_results[1].total_mark,
                    bins=100,
                    kde_kws={"label": "Everyone"}
                )
            except np.linalg.LinAlgError:
                print("NUMPY ERROR -------------------------------------------------")
                # print(demographics_results)
            # x, y = everyone.get_lines()[0].get_data()
            #
            # peaks = findPeaks(x, y)
            # print("peaks: " + str(peaks))
            # plt.vlines(peaks[1][0], 0, peaks[1][1])
            # plt.vlines(peaks[0][0], 0, peaks[0][1])
            try:
                for i in df[demographic].unique():
                    individual = sns.distplot(
                        demographics_results[1][demographics_results[1].gender == i].total_mark,
                        bins = 100,
                        kde_kws={"label": i}
                    )

                plt.xlabel('Total Clicks')
                plt.ylabel('Kernel Density Estimate (KDE)')

                my_path = '/home/marcy/PycharmProjects/MISFITS/'
                my_file = demographic + '_' + str(demographics_results[0]) + '.png'
                plt.savefig(os.path.join(my_path, my_file))
                plt.close()

            except np.linalg.LinAlgError:
                print("numpy error")
                # x, y = individual.get_lines()[0].get_data()
                #
                # plt.plot(x, y)
                #
                # peaks2 = findPeaks(x, y)
                # print("peaks2: " + str(peaks2))
                # plt.vlines(peaks2[1][0], 0, peaks2[1][1])
                # plt.vlines(peaks2[0][0], 0, peaks2[0][1])

            # plt.show()
        except ValueError:
            print ("VALUE ERROR")
            plt.close()

def sort_by_clicks(df, df2):
    total_clicks = findTotalCount(df2)
    master_df =pd.merge(df, total_clicks, on=['id_student', 'code_module', 'code_presentation'])

    print(master_df)
    for demographics_results in master_df.groupby(['code_module', 'code_presentation']):
        my_path = '/home/marcy/PycharmProjects/MISFITS/'
        os.mkdir(my_path + str(demographics_results[0]) + '/')
        my_path = my_path + str(demographics_results[0]) + '/'

        hexplot = sns.jointplot(x = 'total_clicks', y = 'total_mark', data = demographics_results[1])

        my_file = str(demographics_results[0]) + '_scatterplot'  + '.png'
        plt.savefig(os.path.join(my_path, my_file))
        plt.close()

        hexplot = sns.jointplot(x = 'total_clicks', y = 'total_mark', data = demographics_results[1], kind = 'reg')

        my_file = str(demographics_results[0]) + 'linear_regression' + '.png'
        plt.subplots_adjust(top=0.8, bottom=0.2)  # shrink fig so cbar is visible
        plt.savefig(os.path.join(my_path, my_file))
        plt.close()

        hexplot = sns.jointplot(x = 'total_clicks', y = 'total_mark', data = demographics_results[1], kind = 'hex')
        plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)  # shrink fig so cbar is visible
        plt.colorbar()
        my_file = str(demographics_results[0]) + '_hexbins' + '.png'

        plt.savefig(os.path.join(my_path, my_file))
        plt.close()

def findTotalCount(df):
    total_clicks_list = []
    for i in df.groupby(['code_module', 'code_presentation', 'id_student']).sum_click:
        series = i[1]
        total_clicks = series.sum()

        total_clicks_list.append([i[0][0], i[0][1], i[0][2], total_clicks])

    total_clicks_df = pd.DataFrame(total_clicks_list,
                                          columns=['code_module', 'code_presentation', 'id_student', 'total_clicks'])
    return total_clicks_df

def findPeaks(x, y):
    increasing = True
    decreasing = False
    max_value = 0
    turning_points = []
    # print("looking for peaks...")
    # plt.plot(x, y)
    # plt.show()
    # print(y)
    for index, val in enumerate(y):

        if val > 0:
            # print("value" + str(val))
            # print("current max:" + str(max_value))
            if val > max_value:
                # print("------new max value! ---------")
                max_value = val
                increasing = True
            else:
                # print("-----------its decreasing!------------")
                if increasing:
                    # print("---------its a TP!------------")
                    increasing = False
                    turning_points.append([x[index-1], y[index-1]])
                    # print("Found a TP!")
    return turning_points

