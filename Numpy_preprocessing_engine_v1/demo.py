import numpy as np
from engine.pipeline import run_pipeline

np.set_printoptions(suppress=True, precision=2)

def main():
    raw_data = np.array([
        [25, 50000],
        [30, np.nan],
        [25, 50000],
        [45, 120000],
        [100, 999999]
    ])

    print("\n========== RAW DATA ==========")
    print(raw_data)

    steps = [
        ("fill_missing", {"strategies": {1: "median"}}),
        ("remove_duplicates", {}),
        ("cap_outliers", {}),
        ("robust_scale", {})
    ]

    cleaned_data = run_pipeline(raw_data, steps)

    print("\n======== CLEANED DATA ========")
    print(cleaned_data)


    print("\nRaw shape:", raw_data.shape)
    print("Cleaned shape:", cleaned_data.shape)

if __name__ == "__main__":
    main()
