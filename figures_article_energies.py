# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:10:25 2023

@author: Maryelin
"""

# import os
# import numpy as np
# import pandas as pd
# import re
# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
# from scipy import interpolate
# from scipy.signal import savgol_filter
# from scipy.interpolate import make_interp_spline
# from matplotlib.legend_handler import HandlerTuple

# "Dibujo para articulo energies"
# fig, ax = plt.subplots()
# Time = [0, 15, 20, 25, 30]
# iHO  = [0.95, 0.2978, 0.2334, 0.162, 0.0964]
# iLO  = [0.05, 0.4078, 0.4397, 0.4685, 0.5036]
# iGa  = [0.0, 0.0912, 0.1298, 0.1401, 0.1498]
# iCO  = [0.0, 0.1717, 0.1893, 0.2098, 0.2203]

# p1, = ax.plot(Time, iHO, '^', color='tab:blue', markersize=8)
# p2, = ax.plot(Time, iLO, '^', color='tab:green', markersize=8)
# p3, = ax.plot(Time, iGa, '^', color='tab:orange', markersize=8)
# p4, = ax.plot(Time, iCO, '^', color='tab:red', markersize=8)

# folderpath = os.path.join(os.getcwd(),'results(AIRCOND0.5).txt') #AIR conductivity=0.5
# with open(folderpath, 'r') as file:
#     data = pd.read_csv(file, sep=' ', engine='python', header=None)
#     p5, = ax.plot(data.iloc[:,1], data.iloc[:,2], '-', color='tab:blue')
#     p6, = ax.plot(data.iloc[:,1], data.iloc[:,3], '-', color='tab:green')
#     p7, = ax.plot(data.iloc[:,1], data.iloc[:,4], '-', color='tab:orange')
#     p8, = ax.plot(data.iloc[:,1], data.iloc[:,5], '-', color='tab:red')

# labels = ['Heavy Oil', 'Light Oil', 'Gas', 'Coke']
# handles = []
# category1 = ['Simulation Results']
# category2 = ['Experiment Results']

# legend1 = plt.legend([(p1, p5),(p2, p6),(p3, p7),(p4, p8)], ['Heavy Oil', 'Light Oil', 'Gas', 'Coke'], 
#                       numpoints=1,handler_map={tuple: HandlerTuple(ndivide=None)}, 
#                       handlelength=3, fontsize='small', title_fontsize='small')


# ax.grid()       
# ax.set_ylabel('wt %', fontstyle='italic', fontname='Times New Roman', fontsize='12', fontweight='bold')
# ax.set_xlabel('Time (days)', fontstyle='italic', fontname='Times New Roman', fontsize='11', fontweight='bold')

import os
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import interpolate
from scipy.signal import savgol_filter
from scipy.interpolate import make_interp_spline
from matplotlib.legend_handler import HandlerTuple

"Dibujo para articulo energies"
fig, ax = plt.subplots()
Time = [0, 15, 20, 25, 30]
iHO  = [0.95, 0.2978, 0.2334, 0.162, 0.0964]
iLO  = [0.05, 0.4078, 0.4397, 0.4685, 0.5036]
iGa  = [0.0, 0.0912, 0.1298, 0.1401, 0.1498]
iCO  = [0.0, 0.1717, 0.1893, 0.2098, 0.2203]

p1, = ax.plot(Time, iHO, '^', color='tab:blue', markersize=8)
p2, = ax.plot(Time, iLO, '^', color='tab:green', markersize=8)
p3, = ax.plot(Time, iGa, '^', color='tab:orange', markersize=8)
p4, = ax.plot(Time, iCO, '^', color='tab:red', markersize=8)

folderpath = os.path.join(os.getcwd(),'results(AIRCOND0.5).txt') #AIR conductivity=0.5
with open(folderpath, 'r') as file:
    data = pd.read_csv(file, sep=' ', engine='python', header=None)
    p5, = ax.plot(data.iloc[:,1], data.iloc[:,2], '-', color='tab:blue')
    p6, = ax.plot(data.iloc[:,1], data.iloc[:,3], '-', color='tab:green')
    p7, = ax.plot(data.iloc[:,1], data.iloc[:,4], '-', color='tab:orange')
    p8, = ax.plot(data.iloc[:,1], data.iloc[:,5], '-', color='tab:red')

labels = ['Heavy Oil', 'Light Oil', 'Gas', 'Coke']
handles = []
category = ['Simulation Results','Experiment Results']


legend1 = plt.legend([(p1, p5),(p2, p6),(p3, p7),(p4, p8)], labels, 
                     numpoints=1,handler_map={tuple: HandlerTuple(ndivide=None)}, 
                     handlelength=3, fontsize='small', title_fontsize='small')
handles.append(legend1)

line, = ax.plot([],[], linestyle='-', color='black')
point, = ax.plot([],[], marker='^', color='black', markersize=8, linestyle='None', label=None)


legend2 = plt.legend([(line), (point)], category, 
                     numpoints=1,handler_map={tuple: HandlerTuple(ndivide=None)}, 
                     handlelength=3, fontsize='small', title_fontsize='small', bbox_to_anchor=(0.75, 1.0))
     


ax.add_artist(legend1)
ax.add_artist(legend2)
ax.grid()       
ax.set_ylabel('wt %', fontstyle='italic', fontname='Times New Roman', fontsize='12', fontweight='bold')
ax.set_xlabel('Time (days)', fontstyle='italic', fontname='Times New Roman', fontsize='11', fontweight='bold')
plt.show()
