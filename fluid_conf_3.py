# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:48:06 2023

@author: Maryelin
Heavy Oil
ligh oil 
"""

"fluid properties"

from zml import Interp2, TherFlowConfig
import numpy as np


def GAS_den(P, T):
        """
        Table 4, produce gas composition
        """        
        mol = [1.503/100, 73.125/100, 1.031/100, 10.026/100, 9.453/100, 2.497/100, 1.601/100, 0.763/100]
        MW  = [2.016/1000, 28.013/1000, 31.999/1000, 44.01/1000, 16.043/1000, 30.07/1000, 44.097/1000, 58.123/1000]
        TC  = [33.18, 126.10, 154.58, 304.19, 190, 305.42, 369.82, 425.18]
        PC  = [13.13*1.0e5, 33.94*1.0e5, 5.04*1.0e5, 73.82*1.0e5, 46.04*1.0e5, 48.8*1.0e5, 42.49*1.0e5, 37.97*1.0e5 ]
        WC  = [-0.22, 0.04, 0.022, 0.228, 0.011, 0.099, 0.152, 0.199]

        Msc = sum(np.multiply(mol, MW))
        Tsc = sum(np.multiply(mol, TC))
        Psc = sum(np.multiply(mol, PC))
        Wsc = sum(np.multiply(mol, WC))
        
        PM = Msc
        R = 8.314472
        Tc = Tsc
        Pc = Psc
        w  = Wsc
        
        a = 0.42780 * ((R **2) * (Tc**2.5)) / Pc
        b = 0.086640 * (R *  Tc) / Pc
        
        
        # MOLAR VOLUME
        A = - (R * T) / P
        
        B = (1 / P * T**0.5) - ((b * R * T) / P) - (b**2)
        
        C = - (a * b) / (P * T**0.5)
        
        "v_equ = v**3 + A * v**2 + B * v + C"

        
        v_coef = [1, A, B, C]
        v_ = np.roots(v_coef)
        
        den = (1 / (v_.real[0])) * PM
        
        return den
    
def GAS_vis(P, T):
    """
    The same for C11H22
    """
    A = 0.5142
    B = 0.3345
    C = -0.000071071
    viscosity = (A + B*T + (C * (T**2))) * 1.0e-7 #pa*s
    return viscosity

"Heavy Oil"

def Heavy_Oil():
    den = 1007.0  
    vis = 191.6
    specific_heat = 2379.27
    return TherFlowConfig.FluProperty(den=den, vis=vis, specific_heat=specific_heat)

"LIGH OIL"
def Ligh_Oil():
    den = 800.0  
    vis = 0.0015
    specific_heat = 2157.82
    return TherFlowConfig.FluProperty(den=den, vis=vis, specific_heat=specific_heat)

"GAS"

def Gas(tmin=280, tmax=2000, pmin=1.0e6, pmax=40.0e6):
    def gas_den(P, T):
        density = GAS_den(P, T)
        return density

    def get_density(P, T):
        return gas_den(P, T)

    def create_density():
        den = Interp2()
        den.create(pmin, 1e6, pmax, tmin, 10, tmax, get_density)
        return den

    def gas_vis(P, T):
        viscosity = GAS_vis(P, T)
        return viscosity

    def get_viscosity(P, T):
        return gas_vis(P, T)

    def create_viscosity():
        vis = Interp2()
        vis.create(pmin, 1e6, pmax, tmin, 10, tmax, get_viscosity)
        return vis

    specific_heat = 1385.43  # J/kg K
    return TherFlowConfig.FluProperty(den=create_density(), vis=create_viscosity(), specific_heat=specific_heat)


"COKE"

def char():
    den = 1500  # kg/m3
    vis = 1.0e30
    specific_heat = 1380
    return TherFlowConfig.FluProperty(den=den, vis=vis, specific_heat=specific_heat)

def Bitumen():
    den = 1000  # kg/m3 Longmaxi FM (Baoyun Zhao 2021)
    vis = 80.0
    specific_heat = 2200.0  # J/ Kg K # Longmaxi Fm. Xiang etal, 2020
    return TherFlowConfig.FluProperty(den=den, vis=vis, specific_heat=specific_heat)




