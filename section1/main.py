import pandas as pd 
from data_processor import AssignmentDataProcessor as adp 
from data_viz import ExamTrendPlotterPlotly as epp


assign_dp = adp()

if __name__ == "__main__":
    df = pd.read_excel('./docs/Input_v2.xlsx')
    df = assign_dp.preprocessor(df)
    print(df.info())
    print(df.describe())

    # question 1: 
    age_mapper = assign_dp.age_mapper_producer(df)
    data_group_by_age = assign_dp.group_by_age(age_mapper)
    print(len(data_group_by_age))
    print(data_group_by_age)

    # question 2:
    name_list = df.name.to_list()
    final_name_list = assign_dp.middle_vowel_names(name_list)
    print(final_name_list)

    # question 3: 
    df['age_group'] = df['birth_year'].apply(assign_dp.age_group_converter)
    print(df.head())

    # question 4: 
    duplicates = df['id'][df['id'].duplicated()].to_list()
    print(duplicates)

    # question 5: 
    df['age'] = df['birth_year'].apply(assign_dp.age_calculator)    
    df['average'] = df['age_group'].apply(lambda row: assign_dp.avg_age_calculator(df, row))

    # question 6: 
    df['grade']= df.apply(lambda row: assign_dp.grade_calculator(row['assignment_a'],                                         
                                                                    row['assignment_b'],
                                                                    row['mid_term_exam'],
                                                                    row['project'],
                                                                    row['final_exam']
                                                                    ), 
                                                                    axis=1
                                                                )   
    print(df)
    columns_to_include = ['id', 'name', 'birth_year', 'age', 'age_group', 'average']
    # df[columns_to_include].to_csv('./output/final_output.csv', index=False)
    
    # question 7: 
    exam_list = ['assignment_a', 'assignment_b', 'mid_term_exam', 'project', 'final_exam', 'final_grade']
    df['combined'] = df.apply(lambda column: [column['assignment_a'], column['assignment_b'], column['mid_term_exam'], column['project'], column['final_exam'], column['grade']], axis=1)
    graph_plotter = epp(df, exam_list)
    graph_plotter.plot_student_grade_trend('Kirby')







