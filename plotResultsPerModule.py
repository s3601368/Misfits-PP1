import functions as fn
import matplotlib.pyplot as plt
import seaborn as sns

final_grade_module = fn.csv_preview('final_grade_module.csv', 10)
final_grade_module = final_grade_module.drop(0)
for i in final_grade_module.groupby(['code_module', 'code_presentation']):
    course_ID = i[0]
    result_df = i[1]

    print(course_ID)
    print(result_df)
    # for i in result_df['total_mark'].unique():
    #     print(type(i))
    #
    plt.hist(result_df['total_mark'], bins = 100)
    # # sns.distplot(final_grade_module['total_mark'], bins = 100)
    #
    plt.title(str(course_ID))
    plt.xlabel("result")
    plt.ylabel("Number of students")

    plt.show()