# coding: utf-8
import numpy as np

def numerical_gradient(f, x, print_status=False):
    if print_status:
        print('x.shape =', x.shape, 'x.ndim =', x.ndim, '\nx =', x)
    h = 1e-4 # 0.0001
    gradient = np.zeros_like(x)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite']) # x.ndim >= 1 인 경우 모두 가능
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        # f(x+h)
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)
        if print_status:
            print('idx =', idx, 'x+h =', x[idx], 'f(x+h) =', fxh1)
        # f(x-h)
        x[idx] = tmp_val - h 
        fxh2 = f(x)
        if print_status:
            print('idx =', idx, 'x-h =', x[idx], 'f(x-h) =', fxh2)
        gradient[idx] = (fxh1 - fxh2) / (2*h)
        # 값 복원
        x[idx] = tmp_val 
        it.iternext()      
    return gradient