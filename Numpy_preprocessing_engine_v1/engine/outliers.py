import numpy as np
from .validators import validate_array

def detect_iqr(arr):
    arr = validate_array(arr)
    q1 = np.percentile(arr, 25, axis=0)
    q3 = np.percentile(arr, 75, axis=0)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return (arr < lower) | (arr > upper)


def cap_outliers(arr):
    arr = validate_array(arr)
    q1 = np.percentile(arr, 25, axis=0)
    q3 = np.percentile(arr, 75, axis=0)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return np.clip(arr, lower, upper)


def remove_outlier_rows(arr):
    mask = detect_iqr(arr)
    return arr[~mask.any(axis=1)]
