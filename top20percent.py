import functions as fn
import pandas as pd
import numpy as np
chosen_percentile = 0.8
df = fn.csv_preview("studentAssessment.csv")
# filters out top 20th percentile for each class
for i in df['id_assessment'].unique().tolist():
    print("class: " + str(i))
    new_df = df.loc[df['id_assessment'] == i]
    print(new_df)
    percentile = new_df['score'].quantile(chosen_percentile)
    print("Percentile:" + str(percentile))
    df = df.drop(df[(df.id_assessment == i) & (df.score < percentile)].index)
    new_df = df.loc[df['id_assessment'] == i]
    print(new_df)



student_info = fn.csv_preview('studentInfo.csv')
print(student_info)
top_student_list = df['id_student'].unique().tolist()
print("total students" + str(len(top_student_list)))
student_info = student_info[~student_info['id_student'].isin(df['id_student'])]
print(student_info)

df.to_csv(r'20thpercentile.csv')
student_info.to_csv(r'demographics20thpercentile.csv')

