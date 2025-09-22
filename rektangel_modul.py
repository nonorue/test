# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:55:33 2025

@author: nicol
"""

import numpy

def areal_rektangel(lengde, bredde):
    return lengde * bredde

def omkrets_rektangel(lengde, bredde):
    return 2 * (lengde + bredde)

def diagonal_rektangel(lengde, bredde):
    return numpy.sqrt(lengde**2 + bredde**2)