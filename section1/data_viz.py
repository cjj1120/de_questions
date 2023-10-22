import pandas as pd 
import plotly.express as px

class ExamTrendPlotterPlotly:
    def __init__(self, data: pd.DataFrame, exam_list: [str]):
        self.data = data
        self.exam_list = exam_list

    def plot_student_grade_trend(self, student_name: str):
        # Find the row for the specified student name
        student_data = self.data[self.data['name'] == student_name]

        if student_data.empty:
            print(f"Student '{student_name}' not found in the DataFrame.")
            return

        # Get the grades for the specified student
        grades = student_data['combined'].iloc[0]

        # Create a Plotly figure
        fig = px.line(x=range(1, len(grades) + 1), y=grades, labels={'x': 'Exams', 'y': 'Grades'})
        fig.update_layout(
            title=f'Student Grade Trend - {student_name}',
            xaxis=dict(
                tickmode='array',
                tickvals=list(range(1, len(grades) + 1)),
                ticktext=self.exam_list
            ),
            yaxis=dict(range=[0, 110])  # Set the y-axis limits (0-110)
        )

        # Add exam names as labels for each point
        for i, grade in enumerate(grades):
            fig.add_annotation(
                x=i + 1,
                y=grade,
                text=self.exam_list[i],
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowcolor='black'
            )

        # Show the plot for the specified student
        fig.show()
