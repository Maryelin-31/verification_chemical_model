# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 18:44:51 2023

@author: Maryelin

Yaw's corelations'
"""
import numpy as np


def light_oil_vis(P, T):
    A = -4.7333
    B = 918.5
    C = 0.0084
    D = -0.0000080739
    LOGVIS = A + B/T + C*T + D*T**2
    vis_oil = np.exp(LOGVIS) * 0.001
    return vis_oil

