# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 18:50:17 2023

@author: Maryelin

Density of Compressed liquid base on:
Thomson, G. H., Brobst, K. R., & Hankinson, R. W. (1982).
An improved correlation for densities of compressed liquids and liquid mixtures. 
AIChE Journal, 28(4), 671–676. doi:10.1002/aic.690280420

Vapor Pressure by: 
Antoine, C. 1888. Tensions des Vapeurs: Nouvelle Relation Entre les Tensions et les Tempé. Compt.Rend. 107:681-684.
Yaws, Carl L. The Yaws Handbook of Vapor Pressure: Antoine Coefficients. 1 edition. Houston, Tex: Gulf Publishing Company, 2007.

Vs = Saturation liquid Volumen using the packages 
chemicals: Chemical properties component of Chemical Engineering Design Library (ChEDL)
https://chemicals.readthedocs.io/index.html
https://github.com/CalebBell/chemicals

TEMP = (200-750)K
"""
import numpy as np
import chemicals #  pip install chemicals (https://chemicals.readthedocs.io/index.html#installation)


def liq_den_c22h46(P, T):
    #parameters COSTALD
    a = -9.070217
    b = 62.45326
    d = -135.1102
    f = 4.79594
    g = 0.250047
    h = 1.14188
    j = 0.0861488
    k = 0.0344483
    
    #compound properties
    PM = 0.310607 # Kg/mol
    Tc = 791.32 #K
    Pc = 0.902e6 #Pa
    Vc = 1.2675e-3 #m3/mol
    omega = 0.731
    
    #Vapor Pressure Antoine (Yaws Carl)
    t = T - 274.15 #convert kelvin to celsius 
    A = 7.0838
    B = 2054
    C = 120.1
    LOGP = A - (B/(t + C))
    Pv = 10**(LOGP) #convert mmHg to Pa
    Psat = Pv  
    
    #Saturation liquid Volumen
    Vs = chemicals.volume.COSTALD(T, Tc, Vc, omega) # https://chemicals.readthedocs.io/chemicals.volume.html#pure-high-pressure-liquid-correlations
    
    #COSTALD EQUATION
    e = np.exp(f + omega*(g + h*omega))
    C = j + k*omega
    tau = (1.0 - T/Tc)
    tau13 = tau**(1.0/3.0)
    B = Pc*(-1.0 + a*tau13 + b*tau13*tau13 + d*tau + e*tau*tau13)   
    l = (B + P)/(B + Psat)
    V = Vs*(1.0 - C*np.log(l)) #m3/mol
    den = (1 / V) * PM
    return den

# T = np.linspace(200, 750, 100)
# P = np.linspace(1.0e6, 10.0e6, 100)
# for i in T:
#     for j in P:
#         print(liq_den_c22h46(j, i))

# print(liq_den_c22h46(3.5e6, 294))

