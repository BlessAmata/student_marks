import matplotlib.pyplot as plt
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

students_names = ["Blessing","Glory","David", "Susan", "Bath", "Miracle"]
student_marks = [40, 70, 20, 35, 27, 50]
marks_percentage = [40 *100/50, 70 *100/50, 20 *100/50, 35 *100/50, 27 *100/50, 50 *100/50]

def line_chart_of_students_and_marks():
    plt.plot(students_names, student_marks,)
    plt.title("Students marks graph")
    plt.xlabel("Students Names")
    plt.ylabel("Student Marks")
    plt.xlim(xmin = 0, xmax = 6)
    plt.ylim(ymin = 1, ymax = 70)
    plt.grid(True)
    st.pyplot()

def bar_chart_of_students_and_their_percentage():
    left_edges = students_names
    height = marks_percentage
    plt.bar(left_edges, height)
    plt.title("Student Percentages Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Percentages")  
    st.pyplot()

def main():
    st.title("Students Performance Graphs")
    st.write("This application displays the line and bar chart of students' marks and percentages.")
    line_chart_of_students_and_marks()
    bar_chart_of_students_and_their_percentage()

if __name__ == "__main__":
    main()