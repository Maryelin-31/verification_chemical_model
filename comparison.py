# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:32:58 2023

@author: Maryelin
"""

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

"Experiment_nitrogen"

# fig, ax = plt.subplots()
# Time = [0, 15, 20, 25, 30]
# iHO  = [0.95, 0.1947, 0.1056, 0.0826, 0.0525]
# iLO  = [0.05, 0.4537, 0.5225, 0.5427, 0.5650]
# iGa  = [0.0, 0.1266, 0.1524, 0.1631, 0.1662]
# iCO  = [0.0, 0.1572, 0.1898, 0.2042, 0.2138]

# ax.plot(Time, iHO, '^', color='tab:blue' )
# ax.plot(Time, iLO, '^', color='tab:green')
# ax.plot(Time, iGa, '^', color='tab:orange')
# ax.plot(Time, iCO, '^', color='tab:red')

# folderpath = os.path.join(os.getcwd(),'results(NITROGEN_FINAL).txt') #NITROGEN
# with open(folderpath, 'r') as file:
#     data = pd.read_csv(file, sep=' ', engine='python', header=None)
#     ax.plot(data.iloc[:,1], data.iloc[:,2], '--', color='tab:blue')
#     ax.plot(data.iloc[:,1], data.iloc[:,3], '--', color='tab:green')
#     ax.plot(data.iloc[:,1], data.iloc[:,4], '--', color='tab:orange')
#     ax.plot(data.iloc[:,1], data.iloc[:,5], '--', color='tab:red')
#     #SMOOTH
#     yhat2 = savgol_filter((data.iloc[:, 2]), 51, 3)
#     yhat3 = savgol_filter((data.iloc[:, 3]), 51, 3)
#     yhat4 = savgol_filter((data.iloc[:, 4]), 51, 3)
#     yhat5 = savgol_filter((data.iloc[:, 5]), 51, 3)
#     ax.plot(data.iloc[:,1], yhat2, color='tab:blue')
#     ax.plot(data.iloc[:,1], yhat3, color='tab:green')
#     ax.plot(data.iloc[:,1], yhat4, color='tab:orange')
#     ax.plot(data.iloc[:,1], yhat5, color='tab:red')
    
# ax.set_ylabel('wt %', fontstyle='italic', fontname='Times New Roman', fontsize='12', fontweight='bold')
# ax.set_xlabel('Time (days)', fontstyle='italic', fontname='Times New Roman', fontsize='11', fontweight='bold')

"Experiment_air"
fig, ax = plt.subplots()
Time = [0, 15, 20, 25, 30]
iHO  = [0.95, 0.2978, 0.2334, 0.162, 0.0964]
iLO  = [0.05, 0.4078, 0.4397, 0.4685, 0.5036]
iGa  = [0.0, 0.0912, 0.1298, 0.1401, 0.1498]
iCO  = [0.0, 0.1717, 0.1893, 0.2098, 0.2203]


ax.plot(Time, iHO, '^', color='tab:blue', markersize=8)
ax.plot(Time, iLO, '^', color='tab:green')
ax.plot(Time, iGa, '^', color='tab:orange')
ax.plot(Time, iCO, '^', color='tab:red')


folderpath = os.path.join(os.getcwd(),'results_3_.txt') #AIR
with open(folderpath, 'r') as file:
    data = pd.read_csv(file, sep=' ', engine='python', header=None)
    ax.plot(data.iloc[:,1], data.iloc[:,2], '-', color='tab:blue')
    ax.plot(data.iloc[:,1], data.iloc[:,3], '-', color='tab:green')
    ax.plot(data.iloc[:,1], data.iloc[:,4], '-', color='tab:orange')
    ax.plot(data.iloc[:,1], data.iloc[:,5], '-', color='tab:red')
####SMOOTH
    # yhat2 = savgol_filter((data.iloc[:, 2]), 51, 3)
    # yhat3 = savgol_filter((data.iloc[:, 3]), 51, 3)
    # yhat4 = savgol_filter((data.iloc[:, 4]), 51, 3)
    # yhat5 = savgol_filter((data.iloc[:, 5]), 51, 3)
    # ax.plot(data.iloc[:,1], yhat2, color='tab:blue')
    # ax.plot(data.iloc[:,1], yhat3, color='tab:green')
    # ax.plot(data.iloc[:,1], yhat4, color='tab:orange')
    # ax.plot(data.iloc[:,1], yhat5, color='tab:red')
        
ax.set_ylabel('wt %', fontstyle='italic', fontname='Times New Roman', fontsize='12', fontweight='bold')
ax.set_xlabel('Time (days)', fontstyle='italic', fontname='Times New Roman', fontsize='11', fontweight='bold')



