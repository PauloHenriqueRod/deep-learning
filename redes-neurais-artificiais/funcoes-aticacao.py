import numpy as np


def stepFunction(soma):
    if soma >=1 :
        return 1
    return 0

def sigmoidFunction(soma):
    '''
    Usada para problemas binários
    '''
    return 1 / (1+ np.exp(-soma))

def tangenteHiperbolica(soma):
    return (np.exp(soma) - np.exp(-soma))/(np.exp(soma)+np.exp(-soma))

def Relu(soma):
    return soma if soma >=0 else 0

def linearFuncition(soma):
    return soma

def softMax(x):
    ex = np.exp(x)
    return ex/ex.sum()
print(stepFunction(30))
print(sigmoidFunction(2.1))
print(tangenteHiperbolica(2.1))
print((0.7-0.02+0.11-.032)/4)