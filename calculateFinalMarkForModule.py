import functions as fn
import pandas as pd

student_results = fn.csv_preview('studentAssessment.csv', 10)
assessments = fn.csv_preview('assessments.csv', 10)
assessments_search = assessments.set_index("id_assessment", drop = False)
student_total_grade_list = []

for i in assessments.groupby(['code_module', 'code_presentation']).id_assessment:
    course = i[0]
    course_assessments = i[1]
    print(course)
    print(course_assessments)
    student_result_for_module = student_results[student_results['id_assessment'].isin(course_assessments)]
    for j in student_result_for_module.groupby(['id_student']):
        student_id = j[0]
        student_grades = j[1]
        # print ("Results for student: " + str(student_id))
        # print (student_grades)
        final_mark = 0
        exam_flag = False
        for index, row in student_grades.iterrows():
            # print("---------------------------------------------")
            # print(index, row)
            assessment_id = row['id_assessment']
            student_score = row['score']
            weighting = assessments_search.loc[assessment_id, 'weight']
            if weighting == 100:
                exam_flag = True
            # print("assessment_id: " + str(assessment_id))
            # print("weighting: " + str(weighting))
            final_mark = final_mark + (student_score * weighting/100)
            # print ("------------------------------------------------")
        if exam_flag:
            final_mark = final_mark/2
            exam_flag = False

        # print(final_mark)
        student_total_grade_list.append([course[0], course[1], student_id, final_mark])

final_grade_per_module = pd.DataFrame(student_total_grade_list, columns = ['code_module', 'code_presentation', 'id_student', 'total_mark'])
print(final_grade_per_module)
final_grade_per_module.to_csv(r'final_grade_module.csv')