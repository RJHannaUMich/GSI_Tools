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

#labName = "Lab 1: Measurement of Reach Reaction Time (2255648)"
labName = "Lab 1: Measurement of Reach Reaction Time (2466844)"
totalPoints = 24

# opens file dialogue window
Tk().withdraw()
filename = askopenfilename()

# assumes section num is the last 3 characters and rips that
df = pd.read_csv(filename)
df['Section'] = df['Section'].str.slice(start=-3) 

numSections = df['Section'].nunique()
cols = 2 
rows = math.ceil(numSections/2)
fig, axes = plt.subplots(rows,cols,figsize=(10,40),sharey=True, tight_layout=True)

i=0
for g,d in df.groupby('Section'):
    grades=d[labName].to_numpy(dtype='float', na_value=-1)
    ax = plt.subplot(rows, cols, i+1)
    ax.hist(grades, bins=np.append([-1],list(range(totalPoints+1))), label = g)
    ax.set_title(str(g))
    ax.minorticks_on()
    start, end = ax.get_xlim()
    ax.xaxis.set_ticks(np.arange(0, totalPoints+1, 4))
    
    i+=1

plt.savefig('test.png')