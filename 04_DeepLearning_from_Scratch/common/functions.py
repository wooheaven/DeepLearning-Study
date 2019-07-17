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

def cross_entropy_error(y, t):
    if y.ndim == 1: # batch size 1
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    if t.size == y.size: # table : one-hot encoding -> before
        t = t.argmax(axis=1)
             
    batch_size = y.shape[0]
    delta = 1e-7
    return -np.sum(np.log(y[np.arange(batch_size), t] + delta)) / batch_size
