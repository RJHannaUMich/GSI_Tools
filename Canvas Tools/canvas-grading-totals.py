##################################################
# Python file for making the cumulative grade
# reports. 
# 
# Input file is assumed to be the Canvas roster
# that is downloaded from the import groups
# window. 
##################################################

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
import math

# opens file dialogue window
Tk().withdraw()
filename = askopenfilename()

# assumes section num is the last 3 characters and rips that
df = pd.read_csv(filename)
df['Section'] = df['Section'].str.slice(start=-3) 

df = df.head(-1) # removes the test student

# builds the plotting region 
numSections = df['Section'].nunique()
cols = 2 
rows = math.ceil(numSections/2)
fig, axes = plt.subplots(rows,cols,figsize=(10,40),sharey=True, tight_layout=True)

i = 1
for section,data in df.groupby('Section'):
    grades=data['Current Score'].to_numpy(dtype='float', na_value=-1)
    ax = plt.subplot(rows, cols, i)
    ax.hist(grades, bins=np.arange(70, 100, 2).tolist(), label = section)
    ax.set_title(str(section))
    ax.minorticks_on()
    ax.xaxis.set_ticks(np.arange(70, 100, 1))
    i += 1

# opens save dialogue window
Tk().withdraw()
save = asksaveasfilename(filetypes=[('pdf file','*.pdf')], defaultextension=('pdf file','*.pdf'))
plt.savefig(save)