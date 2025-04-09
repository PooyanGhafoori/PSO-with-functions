# -*- coding: utf-8 -*-
"""

@author: Pooyan
"""

from GlobData import GlobalData
import numpy as np
import random

y = GlobalData()

Npop = y[0]
Dimension = y[2]
MinBounds = y[3]
MaxBounds = y[4]
    
def Initialization(Npop, Dimension, MinBounds, MaxBounds):
    Pop =np.zeros([Npop, Dimension])
    for i in range(Npop):
        for j in range(Dimension):
            Pop[i,j] = MinBounds + random.random()*(MaxBounds - MinBounds)
    return Pop
        