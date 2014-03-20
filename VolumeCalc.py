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
