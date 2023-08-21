# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 18:54:10 2023

@author: Maryelin
"""

"""
CHEMICAL

"""

from zml import *
from fluid_conf import *
from zmlx.react import decomposition

def create():

    config = TherFlowConfig()

    # Gas
    config.igas = config.add_fluid(Gas())

    # Heavy Oil
    config.iHO = config.add_fluid(Heavy_Oil())

    # Light Oil
    config.iLO = config.add_fluid(Ligh_Oil())

    # Coke
    config.isol = config.add_fluid(char())

    # The decomposition of Heavy oil
    config.reactions.append(
        decomposition.create(index = config.iHO, iweights=[(config.iLO,  0.5738),   
                                                           (config.igas, 0.1807),
                                                           (config.isol, 0.2455),
                                                           ],
                             temp=623.15, heat=233132.0, 
                             rate=1.19e-6,
                             fa_t=config.flu_keys['temperature'],
                             fa_c=config.flu_keys['specific_heat']))

    return config


if __name__ == '__main__':
    c = create()