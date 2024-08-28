##################################################
# Python file for making the Canvas groups
# 
# Input file is assumed to be the Canvas roster
# that is downloaded from the import groups
# window. 
##################################################

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

import pandas as pd
import math

# opens file dialogue window
Tk().withdraw()
filename = askopenfilename()

# assumes section num is the last 3 characters and rips that
df = pd.read_csv(filename)
df['sections'] = df['sections'].str.slice(start=-3) 

sectionsDF=df.groupby(['sections'])

sortedDF = pd.DataFrame(columns=['name', 'canvas_user_id', 'user_id', 'login_id', 'sections', 'group_name'])
for sectionNum, student in sectionsDF:
    i = 1
    studentList = student
    while i < math.ceil(student.shape[0]/3)+2:
        if studentList.shape[0] != 4:
            if (studentList.shape[0] > 4) or (studentList.shape[0] == 3):  
                group=studentList.sample(n=3, replace=False)
                indexList=group.index.tolist()
                studentList = studentList.drop(indexList)
                group=group.assign(group_name="Section: " + str(sectionNum)+" Lab 1: Group " + str(i))
                sortedDF = sortedDF.append(group)
            else:
                group=studentList.assign(group_name="Section: " + str(sectionNum)+" Lab 1: Group " + str(i))
                indexList=group.index.tolist()
                studentList = studentList.drop(indexList)
                sortedDF = sortedDF.append(group)
        else:
            group=studentList.sample(n=2, replace=False)
            indexList=group.index.tolist()
            studentList = studentList.drop(indexList)
            group=group.assign(group_name="Section: " + str(sectionNum)+" Lab 1: Group " + str(i))
            sortedDF = sortedDF.append(group)

        i= i+1

# opens save dialogue window
Tk().withdraw()
save = asksaveasfilename(filetypes=[('csv file','*.csv')], defaultextension=('csv file','*.csv'))
sortedDF.to_csv(save, index=False)
    
    