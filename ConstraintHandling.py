# -*- coding: utf-8 -*-
"""

@author: Pooyan
"""

from GlobData import GlobalData

Parameters = GlobalData()


Npop = Parameters[0]
Dimension = Parameters[2]
Minbounds = Parameters[3]
Maxbounds = Parameters[4]



def ConstraintHandling(Pop):
    for i in range(Npop):
        for j in range(Dimension):
            if Pop[i,j]<Minbounds:
                Pop[i,j] = Minbounds
            elif Pop[i,j]>Maxbounds:
                Pop[i,j] = Maxbounds

    return Pop