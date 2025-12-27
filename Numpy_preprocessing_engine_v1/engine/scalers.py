import numpy as np
from .validators import validate_array

def min_max_scale(arr):
    arr = validate_array(arr)
    min_v = arr.min(axis=0)
    max_v = arr.max(axis=0)

    denom = np.where(max_v - min_v == 0, 1, max_v - min_v)
    return (arr - min_v) / denom


def z_score_scale(arr):
    arr = validate_array(arr)
    mean = arr.mean(axis=0)
    std = arr.std(axis=0)

    std = np.where(std == 0, 1, std)
    return (arr - mean) / std


def robust_scale(arr):
    arr = validate_array(arr)
    median = np.median(arr, axis=0)
    q1 = np.percentile(arr, 25, axis=0)
    q3 = np.percentile(arr, 75, axis=0)

    iqr = np.where(q3 - q1 == 0, 1, q3 - q1)
    return (arr - median) / iqr
