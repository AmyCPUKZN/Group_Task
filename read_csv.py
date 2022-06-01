# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:25:16 2022

@author: Amy

This code loads data stored in csv files drag or zero_drag. Data is loaded into
a pandas dataframe, df. Each columns of the dataframe is then saved in a numpy array
with appropriate name.

"""


import pandas as pd
import os
import numpy as np

path = os.getcwd()
#name = '/zero_drag'
name = '/drag'

df = pd.read_csv(path+name+'.csv')

# x position
x = np.asarray(df.x)
# y position
y = np.asarray(df.y)
# velocity in the x direction
vx = np.asarray(df.vx)
# velocity in the y direction
vy = np.asarray(df.vy)

# Kinetic energy
Ekin = np.asarray(df.E_kin)
# Potential energy
Epot = np.asarray(df.E_pot)
# Total energy
Etot = np.asarray(df.E_total)

