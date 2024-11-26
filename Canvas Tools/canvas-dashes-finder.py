##################################################
# Python file for identifying students who still 
# have dashes, sorts them by section, and 
# lists what labs they missed. 
#
# Input file is assumed to be the Canvas grades
# file that is downloaded from the gradebook 
# view. 
##################################################

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import matplotlib
matplotlib.use('Agg')
import pandas as pd

uptoLab = 10 #change to scan through up to lab # whatever

# opens file dialogue window
Tk().withdraw()
filename = askopenfilename()

# assumes section num is the last 3 characters and rips that
df = pd.read_csv(filename)
df['Section'] = df['Section'].str.slice(start=-3) 

df = df.head(-1) # removes the test student

# opens save dialogue window
Tk().withdraw()
save = asksaveasfilename(filetypes=[('txt file','*.txt')], defaultextension=('txt file','*.txt'))

file = open(save, "w")
for section,data in df.groupby('Section'):
    file.write("\n"+"=== Section: "+str(section)+ " ===" + "\n"+"\n")
    for index in range(1, uptoLab+1, 1):
        string = 'Lab '+str(index)+':'
        labsArray = data.loc[:,data.columns.str.startswith((string, "Student"))]
        if labsArray[labsArray.isna().any(axis=1)].empty == True:
            file.write(string+" completed!"+"\n"+ "=-=-=-=-=-=-=-=-=" +"\n")
        else:
            namesArray = labsArray[labsArray.isna().any(axis=1)].to_string(index=False)
            file.write(string+"\n"+ "=-=-=-=-=-=-=-=-=" +"\n")
            file.write(namesArray+"\n"+ "=-=-=-=-=-=-=-=-=" +"\n")

file.close()