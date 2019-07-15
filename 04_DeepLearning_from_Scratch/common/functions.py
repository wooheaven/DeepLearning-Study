import numpy as np

def softmax(x, print_status=False):
    if print_status:
        print('softmax', x.shape, x.ndim, x)
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0) # overflow
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T 
    x = x - np.max(x) # overflow
    return np.exp(x) / np.sum(np.exp(x))