# -*- coding: utf-8 -*-
"""

@author: Pooyan
"""

from GlobData import GlobalData
import numpy as np

y = GlobalData()

Npop = y[0]
Dimension = y[2]
MinBounds = y[3]
MaxBounds = y[4]



f = np.zeros([Npop,1])
def Eval(Npop, Dimension,Pop):
    for i in range(Npop):
        s = 0
        for j in range(Dimension):
            s = s + Pop[i,j]**2 
            
        f[i] = s
    return f    
    
