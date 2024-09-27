import numpy as np

def calculate(list):
   
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matriz = np.array(list).reshape(3, 3)
    
    mean = [np.mean(matriz, axis=0).tolist(), np.mean(matriz, axis=1).tolist(), np.mean(matriz)]
    
    variance = [np.var(matriz, axis=0).tolist(), np.var(matriz, axis=1).tolist(), np.var(matriz)]
    
    std_dev = [np.std(matriz, axis=0).tolist(), np.std(matriz, axis=1).tolist(), np.std(matriz)]
    
    max_val = [np.max(matriz, axis=0).tolist(), np.max(matriz, axis=1).tolist(), np.max(matriz)]
    
    min_val = [np.min(matriz, axis=0).tolist(), np.min(matriz, axis=1).tolist(), np.min(matriz)]

    sum_val = [np.sum(matriz, axis=0).tolist(), np.sum(matriz, axis=1).tolist(), np.sum(matriz)]

    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }
    
    return calculations

result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)