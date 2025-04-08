from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import matplotlib
matplotlib.use('Agg')
import pandas as pd

uptoQuiz = 12 #change to scan through up to lab # whatever
flag = 151

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
    for index in range(1, uptoQuiz+1, 1):
        string = 'Quiz '+str(index)+':'
        labsArray = data.loc[:,data.columns.str.startswith((string, "Student"))]
        # 251 optional Quiz to radiation:
        lab12A = data.loc[:, data.columns.str.startswith((string, "Lab 12A: Nerve Action II", "Student"))] 
        if index == 12 and flag == 251:
            namesArray1 = lab12A[lab12A.iloc[:,1:].isnull().all(axis=1)]
            namesArray2 = lab12A[lab12A.notnull().all(axis=1)]
            if namesArray1.empty and namesArray2.empty:
                file.write(string+" completed!"+"\n")
            elif namesArray2.empty: 
                file.write("Quiz 12 and 12A:"+"\n"+ "=-=-=-=-=-=-=-=-=" +"\n")
                file.write(namesArray1.to_string(index=False, header=False)+"\n"+ "=-=-=-=-=-=-=-=-=" +"\n")
            elif namesArray1.empty:
                file.write("These student(s) have submissions for both Quiz 12 and 12A:"+"\n")
                file.write(namesArray2.to_string(index=False, header=False)+"\n"+ "=-=-=-=-=-=-=-=-=" +"\n")    
            else:
                file.write("Quiz 12 and 12A:"+"\n")
                file.write(namesArray1.to_string(index=False, header=False)+"\n"+ "=-=-=-=-=-=-=-=-=" +"\n")
                file.write("These student(s) have submissions for both Quiz 12 and 12A:"+"\n")
                file.write(namesArray2.to_string(index=False, header=False)+"\n"+ "=-=-=-=-=-=-=-=-=" +"\n")
        elif labsArray[labsArray.isna().any(axis=1)].empty == True:
            file.write(string+" completed!"+"\n"+ "=-=-=-=-=-=-=-=-=" +"\n")
        else:
            namesArray = labsArray[labsArray.isna().any(axis=1)].to_string(index=False, header=False)
            file.write(string+"\n")
            file.write(namesArray+"\n"+ "=-=-=-=-=-=-=-=-=" +"\n")

file.close()