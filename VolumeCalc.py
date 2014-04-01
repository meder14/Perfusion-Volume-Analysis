# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 12:34:37 2014

@author: Ty
"""
from __future__ import division
from numpy import pi
#NOTE: all radii are inner radii, not outer
# dimensions for the bioreactor tube that feeds into the chamber
r_biotube = 0.0015875  #1/16th inch diameter
l_biotube = 0.05  #**REFER TO L_midtube**

# dimensions for the bioreactor syringe
r_biosyr = 0.012446/2   #0.49 inch diameter
l_biosyr = 0.035   # **length between CLAMP and END** 3.5 cm

V_bio = pi*(r_biotube**2*l_biotube + r_biosyr**2*l_biosyr)

# dimensions for the manifold
r_manif = 0.003175/2  #1/8 inch diameter
l_manif = 0.035  #length of main part of the manifold
l_split = 0.035/5  #length of one of the split pieces (5 of them per manifold)

V_manif = pi*r_manif**2*(l_manif + 5*l_split)

# dimensions for the outflow tubes (from bioreactor)
r_outtube = 0.003175/2  #1/8th inch diameter
l_outtube = 0.1  #0.1 m

V_outtube = pi*r_outtube**2*l_outtube

# dimensions for the tube between manifold and bioreactor tube
r_midtube = 0.0015875/2  #1/16th inch diameter
l_midtube = 0.05  # **the 0.1m is shared between this and l_biotube

V_midtube = pi*r_midtube**2*l_midtube

# dimensions of the tube from manifold to manifold (main to branch)
r_intube = 0.003175/2  #1/8th inch diameter
l_intube = 0.05  #0.05 m

V_intube = pi*r_intube**2*l_intube

# dimensions of the main line in to the main manifold
r_main = 0.00635/2
l_main = 3.0

V_main = pi*r_main**2*l_main

# combine volumes

V_total = 20*V_bio + 5*V_manif + V_outtube*20 + V_midtube*5 + V_intube
print V_total