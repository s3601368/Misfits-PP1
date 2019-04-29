import pandas as pd
import glob

# df = pd.read_csv('assessments.csv')
# print (df.info())
dataframes = []


# for fname in glob.glob("*.csv"):
#     dataframes.append(pd.read_csv(fname))
#
# for i in dataframes:
#     print(i.head())

studentVle = pd.read_csv("studentVle.csv")
studentInfo= pd.read_csv("studentInfo.csv")
studentInfo = studentInfo.drop(["gender", "imd_band", "highest_education", "age_band",
                                "studied_credits", "region", "disability"], axis = 1)
print(studentVle.head())
studentVle = studentVle.drop(["id_site", "date"], axis = 1)
print(studentVle.head())

studentVle = studentVle.groupby(["code_module", "id_student",  "code_presentation"]).sum()

studentVle = pd.merge(studentVle, studentInfo, on='id_student', how='outer')
print(studentVle.head())

studentVle.to_csv(r'clicksvsresult.csv')