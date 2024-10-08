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

df = df.head(-1)

# builds the plotting region 
numSections = df['Section'].nunique()
cols = 2 
rows = math.ceil(numSections/2)
fig, axes = plt.subplots(rows,cols,figsize=(10,40),sharey=True, tight_layout=True)

# tabulates the number of dashes
i = 1 
for section,data in df.groupby('Section'):
    totalLabs = 12 
    percentArray = np.zeros(shape=(12,4))
    for index in range(1, totalLabs+1, 1):
        string = 'Lab '+str(index)+':'
        labCol = data.filter(regex=string)
        dashes = float(labCol.isnull().sum().sum())
        nondashes = float(labCol.notnull().sum().sum())
        zeros = float((labCol == 0).sum().sum())
        if (math.isnan(dashes)) or (math.isnan(nondashes)):
            percentNon = 0
            percentDash = 1 
            percentZero = 0
        elif (nondashes == 0):
            percentNon = 0
            percentDash = 1 
            percentZero = 0
        else:
            total = dashes + nondashes
            percentNon = (nondashes-zeros)/total
            percentDash = dashes/total 
            percentZero = zeros/total 
        percentArray[1-index] = [index, percentNon, percentZero, percentDash] 
    
    ax = plt.subplot(rows, cols, i)
    ax.bar(percentArray[:,0],percentArray[:,1], label='Completed', color='g')
    ax.bar(percentArray[:,0],percentArray[:,2], bottom=percentArray[:,1], label='Zeros', color='b')
    ax.bar(percentArray[:,0],percentArray[:,3], bottom=percentArray[:,1]+percentArray[:,2], label='Dashes', color='r')

    ax.set_title(str(section))
    ax.set_xticks(percentArray[:,0])
    ax.legend()
    i += 1

# opens save dialogue window
Tk().withdraw()
save = asksaveasfilename(filetypes=[('pdf file','*.pdf')], defaultextension=('pdf file','*.pdf'))
plt.savefig(save)