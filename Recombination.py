# -*- coding: utf-8 -*-
"""

@author: Pooyan
"""

from GlobData import GlobalData
import random as random
import numpy as np

Parameters = GlobalData()
Npop = Parameters[0]
Iter = Parameters[1]
Dimension = Parameters[2]

c1i = 2.5
c1f = 0.5
c2i = 0.5
c2f = 0.6
r1 = np.zeros([1,Dimension])
r2 = np.zeros([1,Dimension])
def rec(GBest, PBest, Pop, Velocity, k, Iter):
    c1 = c1i +  (c1f - c1i)*k/Iter
    c2 = c2i +  (c2f - c2i)*k/Iter
    omega = 0.9 + (.4 - 0.9)*k/Iter
    for i in range(Npop):
        for j in range(Dimension):
            r1 = random.random()
            r2 = random.random()
            Velocity[i,j] = omega*Velocity[i,j] + c1*r1*(PBest[i,j] - Pop[i,j]) + c2*r2*(GBest[j] - Pop[i,j])

    Pop = Pop + Velocity
  
    return Pop, Velocity







