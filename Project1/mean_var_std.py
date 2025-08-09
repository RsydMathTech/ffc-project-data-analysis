import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(numbers).reshape(3, 3)

    def stat(fn):
        return [
            fn(arr, axis=0).tolist(),
            fn(arr, axis=1).tolist(),
            fn(arr).item()
        ]

    return {
        'mean': stat(np.mean),
        'variance': stat(np.var),
        'standard deviation': stat(np.std),
        'max': stat(np.max),
        'min': stat(np.min),
        'sum': stat(np.sum)
    }