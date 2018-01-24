    display(ds.head(10))
import numpy as np
import scipy as sp

def pearson(x, y):
    return sp.stats.pearsonr(x, y)