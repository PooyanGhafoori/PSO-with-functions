

import numpy as np
import matplotlib.pyplot as plt


from GlobData import GlobalData
# GlobalData = [Npop, NIter, Dimension, MinBounds, MaxBounds]
from Initialization import Initialization
from Evaluation import Eval
from BestSelection import BestSel
from Recombination import rec
from ConstraintHandling import ConstraintHandling

Parameters = GlobalData()
print(Parameters[1])
Npop = Parameters[0]
NIter = Parameters[1]
Dimension = Parameters[2]

IniPop = Initialization(Npop, Dimension, Parameters[3], Parameters[4],)
PBestValue = np.zeros([Npop,1])
f = Eval(Npop, Dimension,IniPop)

for i in range(Npop):
    PBestValue[i] =f[i]

#PBestValue = f

PBest = IniPop 

GBestValue = min(PBestValue)

GBestindex = np.argmin(GBestValue)
GBest = PBest[GBestindex]
Pop = IniPop
Velocity = np.zeros([Npop,Dimension])
BestOut = np.zeros([NIter,1])

for k in range(0,NIter,1):
    [Pop, Velocity] = rec(GBest, PBest, Pop, Velocity, k, NIter)
    Pop = ConstraintHandling(Pop)
    f = Eval(Npop, Dimension,Pop)
    [PBest, PBestValue, GBest, GBestValue] = BestSel(f, Pop, PBestValue, PBest)


    BestOut[k] = GBestValue
    print('PBest',PBestValue)
    
plt.figure()
x = np.arange(1,NIter+1,1)
plt.plot(x,BestOut)  
plt.show()  
#print(Pop)