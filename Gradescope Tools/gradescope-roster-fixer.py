##################################################
# Python file for merging physics and biophysics 
# students into the same section for gradescope
# roster. 
#
# Assumes that the input file is the gradebook 
# roster as downloaded from Gradescope after it 
# has been synced with Canvas. 
##################################################

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

import pandas as pd

# opens file dialogue window
Tk().withdraw()
filename = askopenfilename()

# assumes section num is the last 3 characters and rips that
df = pd.read_csv(filename)
df['Section'] = df['Section'].str.slice(start=-3)

# opens save dialogue window
Tk().withdraw()
save = asksaveasfilename(filetypes=[('csv file','*.csv')], defaultextension=('csv file','*.csv'))
df.to_csv(save, index=False)