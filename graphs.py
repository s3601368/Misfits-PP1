import functions as fn
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
chosen_percentile = 0.8


assessments = fn.csv_preview('assessments.csv')
student_assessments = fn.csv_preview('studentAssessment.csv')
demographics = fn.csv_preview('studentInfo.csv')

print( assessments[assessments['assessment_type'] == 'Exam'])

exams_df = assessments[assessments['assessment_type'] == 'Exam']
print(exams_df)

student_scores = student_assessments[student_assessments['id_assessment'].isin(exams_df['id_assessment'])]
print(student_scores)

demographics = demographics[demographics['id_student'].isin(student_scores['id_student'])]

percentile = student_scores['score'].quantile(chosen_percentile)

# remove this line for ALL scores, keep this line for top 20% of results
student_scores = student_scores[student_scores.score > percentile]


merged_dataframe = pd.merge(student_scores, demographics.rename(columns={'id_student': 'id_student'}),
                            on='id_student', how='left')
print(merged_dataframe)

