# -*- coding: utf-8 -*-
"""

@author: Pooyan
"""

import numpy as np
from GlobData import GlobalData

Parameters = GlobalData()
Npop = Parameters[0]
Dimension = Parameters[2]
Minbounds = Parameters[3]
Maxbounds = Parameters[4]



def BestSel(f, Pop, PBestValues, PBest):
    for i in range(Npop):
        if f[i]<PBestValues[i]:
            PBestValues[i] = f[i]
            PBest[i]=Pop[i]
            print(f[i])

    GBestValue = min(PBestValues)
#    print(GBestValue0)
#    GlobalBestInbdex = f.index(GlobalFun)
    IndexGBest = np.argmin(PBestValues)
    GBest = PBest[IndexGBest]
  
  
    return PBest, PBestValues, GBest, GBestValue



