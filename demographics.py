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
fn.sort_by_demographics(demographics_result, 'age_band')
# for demographics_results in demographics_result.groupby(['code_module', 'code_presentation']):
#
#     sns.distplot(demographics_results[1].total_mark, bins = 100)
#     sns.distplot(demographics_results[1][demographics_results[1].gender == "F"].total_mark, bins = 100)
#     sns.distplot(demographics_results[1][demographics_results[1].gender == "M"].total_mark, bins = 100)
#
#     plt.show()
