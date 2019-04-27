import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt


data = []
def ndarray_to_string_list(ndarry):
    list = ndarry.tolist()
    str_list = [str(i) for i in list]
    return str_list

def select_rows(df,search_strings):
    unq,IDs = np.unique(df,return_inverse=True)
    unqIDs = np.searchsorted(unq,search_strings)
    return df[((IDs.reshape(df.shape) == unqIDs[:,None,None]).any(-1)).all(0)]

def display_csv_files():
    for files in glob.glob("*.csv"):
        print(files)


def display_sample_data():
    for files in glob.glob("*.csv"):
        print(files)
        data = pd.read_csv(files)
        print(data.head())


def load_data():
    for files in glob.glob("*.csv"):
        data.append([files, pd.read_csv(files)])
    print("data loaded!")

def sample_plot():
    print("Starting sample plot...")
    # quick sample plot of student grades vs age
    load_data()
    studentAssessment = pd.DataFrame()
    studentInfo = pd.DataFrame

    for csv, dataframe in data:
        if csv == "studentAssessment.csv":
            studentAssessment = dataframe
            print("studentAssessment loaded")
        if csv == "studentInfo.csv":
            studentInfo = dataframe
            print("studentInfo loaded")
    #prints first 5 lines
    print(studentAssessment.head())
    print(studentInfo.head())
    merged_dataframe = pd.merge(studentAssessment, studentInfo.rename(columns={'id_student': 'id_student'}), on='id_student', how='left')
    print(merged_dataframe.head())

    assessmentIDs = merged_dataframe.id_assessment.unique()
    # print(assessmentIDs)

    final_df = merged_dataframe[merged_dataframe.id_assessment == assessmentIDs[0]]

    final_df.plot.scatter(x = 'date_submitted', y='score')
    plt.show()

    # unique_studentID = unique_results.id_student.unique()
    # print (studentInfo.head())
    # id = studentInfo.id_student.unique()
    # unique_studentInfo = select_rows(studentInfo, [id[0]])
    # print(unique_studentInfo)

def main():
    print("Select one of the following options:")
    print("1. Display csv files")
    print("2. Show sample data")
    print("3. Load data")
    print("4. Sample plot")

    user_input = input()
    if int(user_input) == 1:
        display_csv_files()
    if int(user_input) == 2:
        display_sample_data()
    if int(user_input) == 3:
        load_data()
    if int(user_input) == 4:
        sample_plot()




if __name__ == "__main__":
    main()
