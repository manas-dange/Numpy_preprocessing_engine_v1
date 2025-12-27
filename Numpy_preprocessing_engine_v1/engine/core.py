import numpy as np
from .validators import validate_array

def fill_missing(arr, strategies):
    """
    strategies: dict {col_index: 'mean' | 'median' | number}
    """
    arr = validate_array(arr)
    result = arr.copy()

    for col, strategy in strategies.items():
        col_data = result[:, col]
        mask = np.isnan(col_data)

        if not mask.any():
            continue

        if strategy == "mean":
            value = np.nanmean(col_data)
        elif strategy == "median":
            value = np.nanmedian(col_data)
        elif isinstance(strategy, (int, float)):
            value = strategy
        else:
            raise ValueError("Invalid fill strategy")

        result[mask, col] = value

    return result


def remove_duplicates(arr):
    arr = validate_array(arr)
    return np.unique(arr, axis=0)
