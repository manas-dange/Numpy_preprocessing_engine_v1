import numpy as np

def validate_array(arr):
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a NumPy array")

    if arr.size == 0:
        raise ValueError("Array is empty")

    if arr.ndim != 2:
        raise ValueError("Only 2D arrays are supported")

    if not np.issubdtype(arr.dtype, np.number):
        raise TypeError("Array must contain numeric data only")

    return arr.astype(float)
