# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 12:34:37 2014

@author: Ty
"""
from numpy import pi
#NOTE: all radii are inner radii, not outer
# dimensions for the bioreactor tube that feeds into the chamber
r_biotube = 0
l_biotube = 0
# dimensions for the bioreactor syringe
r_biosyr = 0
l_biosyr = 0

V_bio = pi*(r_biotube**2*l_biotube + r_biosyr**2*l_biosyr)

# dimensions for the manifold
r_manif = 0
l_manif = 0  #length of main part of the manifold
l_split = 0  #length of one of the split pieces (5 of them per manifold)

V_manif = pi*r_manif**2*(l_manif + 5*l_split)

# dimensions for the outflow tubes (from bioreactor)
r_outtube = 0
l_outtube = 0

V_outtube = pi*r_outtube**2*l_outtube

# dimensions for the tube between manifold and bioreactor
r_midtube = 0
l_midtube = 0

V_midtube = pi*r_midtube**2*l_midtube

# dimensions of the tube from manifold to manifold (main to branch)
r_intube = 0
l_intube = 0

V_intube = pi*r_intube**2*l_intube

# dimensions of the main line in to the main manifold
r_main = 0
l_main = 0

V_main = pi*r_main**2*l_main

# combine volumes

V_total = 20*V_bio + 5*V_manif + V_outtube*20 + V_midtube*5 + V_intube