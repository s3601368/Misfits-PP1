import functions as fn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
final_grade_module = fn.csv_preview('final_grade_module.csv', 10)
demographics = fn.csv_preview('studentInfo.csv', 10)
final_grade_module = final_grade_module.drop(0)

demographics_result = pd.merge(final_grade_module, demographics, on=['id_student', 'code_module', 'code_presentation'])

print(demographics_result.head(20))
studentVle = fn.csv_preview('studentVle.csv', 10)
total_clicks = fn.findTotalCount(studentVle)
master_df = pd.merge(demographics_result, total_clicks, on=['id_student', 'code_module', 'code_presentation'])

# fn.sort_by_clicks(demographics_result, studentVle)
demographic = ['gender', 'region', 'highest_education', 'imd_band', 'age_band', 'num_of_prev_attempts', 'studied_credits', 'disability', 'final_result']
# fn.plot_demographic_amounts(master_df, demographic)
fn.sort_by_demographics(master_df, 'gender')