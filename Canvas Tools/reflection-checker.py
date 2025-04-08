##################################################
# Python file for compairing the exams to the 
# reflections to make sure a student has not 
# received more points than they have lost.
# 
# Input file is assumed to be the Canvas grade-
# book and the download grades csv from gradescope.
# 
##################################################

# imports
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pandas as pd

# columns to check
exam = "Midterm 2 (2699106)"
reflection = "1: Problems reworked: 0.25 per corrected problem (5.0 pts)"

# opens Canvas file dialogue window
Tk().withdraw()
filenameCanvas = askopenfilename(title="Select the Canvas Gradebook CSV.")

canvas_df = pd.read_csv(filenameCanvas)
canvas_df = canvas_df.head(-1) # removes the test student

canvasNameGrade = canvas_df[["Student", exam]]
canvasNameGrade= canvasNameGrade.rename(columns={"Student":"Name"})


# opens Gradescope file dialogue window
Tk().withdraw()
filenameGradescope = askopenfilename(title="Select the Gradescope Grades CSV.")

gradescope_df = pd.read_csv(filenameGradescope)

gradescopeNames = gradescope_df["Last Name"].map(str) + ", " + gradescope_df["First Name"].map(str)
gradescopeGrade = gradescope_df[reflection]
gradescopeNameGrade = pd.concat([gradescopeNames,gradescopeGrade], axis=1)
gradescopeNameGrade = gradescopeNameGrade.rename(columns={0:"Name"})

# checks to make sure no student scored above 20/20 with the reflection corrections 
merged_df = pd.merge(canvasNameGrade,gradescopeNameGrade, on="Name",how="inner" )
merged_df["checker"] = merged_df[reflection] + merged_df[exam]
merged_df["checker"] = merged_df["checker"].gt(20)
print(f"There are students with scores greater than 20/20:  {merged_df.loc[merged_df["checker"]==True]}")