import numpy as np
import array as arr

def calculate(list):
    
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")

    values = np.reshape(list, (3,3))
    
    calculations = {
    'mean': [np.mean(values, axis = 0).tolist(), np.mean(values, axis = 1).tolist(), np.mean(values).tolist()],
    'variance': [np.var(values, axis = 0).tolist(), np.var(values, axis = 1).tolist(), np.var(values).tolist()],
    'standard deviation': [np.std(values, axis = 0).tolist(), np.std(values, axis = 1).tolist(), np.std(values).tolist()],
    'max': [np.max(values, axis = 0).tolist(), np.max(values, axis = 1).tolist(), np.max(values).tolist()],
    'min': [np.min(values, axis = 0).tolist(), np.min(values, axis = 1).tolist(), np.min(values).tolist()],
    'sum': [np.sum(values, axis = 0).tolist(), np.sum(values, axis = 1).tolist(), np.sum(values).tolist()]
    }

    return calculations