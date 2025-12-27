from .core import fill_missing, remove_duplicates
from .scalers import min_max_scale, z_score_scale, robust_scale
from .outliers import cap_outliers, remove_outlier_rows

def run_pipeline(arr, steps):
    """
    steps: list of tuples
    [
      ("fill_missing", {"strategies": {0: "mean"}}),
      ("remove_duplicates", {}),
      ("robust_scale", {})
    ]
    """
    data = arr

    for step, config in steps:
        if step == "fill_missing":
            data = fill_missing(data, **config)
        elif step == "remove_duplicates":
            data = remove_duplicates(data)
        elif step == "min_max_scale":
            data = min_max_scale(data)
        elif step == "z_score_scale":
            data = z_score_scale(data)
        elif step == "robust_scale":
            data = robust_scale(data)
        elif step == "cap_outliers":
            data = cap_outliers(data)
        elif step == "remove_outlier_rows":
            data = remove_outlier_rows(data)
        else:
            raise ValueError(f"Unknown step: {step}")

    return data
