import numpy as np
import scipy as sp

def pearson(x, y):
    if len(x.shape) == 1:
        x = x.reshape((1, -1))
    if len(y.shape) == 1:
        y = y.reshape((1, -1))
        
    prsn = np.zeros((x.shape[0], y.shape[0]))
    for xi in np.arange(x.shape[0]):
        for yi in np.arange(y.shape[0]):
            prsn[xi, yi] = sp.stats.pearsonr(x[xi,:], y[yi,:])[0]
    
    return prsn
