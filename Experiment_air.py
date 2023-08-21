## -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:47:24 2023

@author: Maryelin

Experimental study on thermal cracking reactions of ultra-heavy oils during 
air injection assisted in-situ upgrading process
"""
from zml_hyd import *
from kineticReaction_3 import create
import numpy as np

mesh = SeepageMesh.create_cylinder(np.linspace(0, 134*0.001, 11), np.linspace(0, (63*0.001)/2, 6))

x1, x2 = mesh.get_pos_range(0)
cells_x1 = mesh.get_cells_in_range(xr=(x1 - 0.01, x1 + 0.01))
cells_x2 = mesh.get_cells_in_range(xr=(x2 - 0.01, x2 + 0.01))


def get_initial_t(x, y, z):
    return 304.15 + 22.15 - 0.0443 * x

def get_initial_p(x, y, z):
    return 3.2e6 + 20.0e6 - 1e4 * x


def get_perm(x, y, z):
    """
    the initial permeability 
    """
    return 1.5e-16

def get_initial_s(x, y, z):
    """
    the initial saturation of phase (Gas, Heavy Oil, Light Oil, Coke)
    """
    return 0.0, 0.95, 0.05, 0.0


config = create()
model = config.create(mesh, porosity=0.05, pore_modulus=1000e6, denc=2600*3000, dist=1.0,
                      temperature=get_initial_t, p=get_initial_p,
                      s=get_initial_s, perm=get_perm, heat_cond=0.5)

# for cell in model.cells:
#     print(cell.fluid_number)

inj_cells = cells_x1 

for c in inj_cells:
    cell = config.add_cell(model)
    cell.set_attr(config.cell_keys['temperature'], 624.15)
    cell.set_attr(config.cell_keys['mc'], 1.0e20)
    face = config.add_face(model, model.get_cell(cell.index), model.get_cell(c.index))
    face.set_attr(config.face_keys['g0'], 0)
    face.set_attr(config.face_keys['g_heat'], 0.0)
    

def mass(fid):
    masa = []
    for cell in model.cells:
        masa.append(cell.get_fluid(fid).mass)    
    return sum(masa)
# print(mass(1))

def saturation(fid):
    total_vol = []
    vol_fluid = []
    for cell in model.cells:
        Cell_Fluid_Vol = 0
        vol_fluid.append(cell.get_fluid(fid).mass)
        for fluid in range(cell.fluid_number):
            Cell_Fluid_Vol += cell.get_fluid(fluid).mass
        total_vol.append(Cell_Fluid_Vol)
    total = sum(total_vol)
    total_fluid = sum(vol_fluid)
    saturation = total_fluid/total
    return saturation

def pressure_cracking(): 
    """
    Pressure changes of thermal cracking experiments
    """
    for cell in model.cells:
        temp = cell.get_attr(config.cell_keys['temperature'])
        cell.set_attr(config.cell_keys['pre'], 0.0523 * temp + 8.1145 )
    return 

def Save(path, step):
    assert isinstance(path,str)
    Savefolder = os.path.join(os.getcwd(), f'Pressure(1)')
    SavePath = os.path.join(Savefolder, path)
    with open(SavePath, 'w') as file:
        for cell in model.cells:
            pressure = cell.pre
            # temp = cell.get_attr(config.cell_keys['temperature'])
            # pressure = cell.set_attr(config.cell_keys['pre'], 0.0884 * temp + 10.019 )
            file.write(f'{pressure}\n')
            

def run(): 
    solver = ConjugateGradientSolver()
    solver.set_tolerance(1.0e-13)
    import zml
    import shutil
    shutil.rmtree(zml.data.folder)
    with open(f'results_3_.txt', 'w') as f:
        for step in range(1000000000000000):
            config.iterate(model, solver=solver)
            # pressure_cracking()
            if config.get_time(model) > 3600 * 24 * 30:           
                print(f'{step}, Finish')
                break
            if step % 1000 == 0:
                sat_gas = saturation(0)
                sat_HO  = saturation(1)
                sat_LO  = saturation(2)
                sat_CO  = saturation(3)
                # Save(path, step)
                f.write(f'{step} {config.get_time(model) / (3600 * 24)} {sat_HO} {sat_LO} {sat_gas} {sat_CO}\n')
                print(f'{step}, time = {config.get_time(model) / (3600 * 24)},  heavy oil = {sat_HO}, ')         
run()