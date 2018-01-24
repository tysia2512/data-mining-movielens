import numpy as np
import scipy as sp

def pearson(x, y):
    if len(x.shape) == 1:
        x = x.reshape((1, -1))
    if len(y.shape) == 1:
        y = y.reshape((1, -1))

    prsn = np.zeros((x.shape[0], y.shape[0])
    for xv in enumerate(x):
        for yv in enumerate(y):
            prsn[(xv[0], yv[0])] = sp.stats.pearsonr(xv[1], yv[1])
    
    return prsn
