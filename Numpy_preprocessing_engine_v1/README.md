
<pre class="overflow-visible! px-0!" data-start="0" data-end="1328"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-md"><span><span># NumPy Preprocessing Engine</span><span>

A NumPy-only preprocessing engine for structured numeric data.

This project is intentionally built without Pandas to understand how data preprocessing works at a low level and to expose data-cleaning tradeoffs that are usually hidden behind high-level abstractions.

---

</span><span>## Scope</span><span>

This engine:
</span><span>-</span><span> Accepts numeric NumPy arrays only
</span><span>-</span><span> Operates on 2D tabular data
</span><span>-</span><span> Focuses strictly on preprocessing logic
</span><span>-</span><span> Does not include modeling or visualization

It is designed for learning, analysis, and interview demonstration, not for production pipelines.

---

</span><span>## Features</span><span>

</span><span>### Input Validation</span><span>
</span><span>-</span><span> Enforces NumPy array input
</span><span>-</span><span> Ensures numeric data types
</span><span>-</span><span> Rejects empty or malformed arrays

</span><span>### Missing Value Handling</span><span>
</span><span>-</span><span> Column-wise strategies
</span><span>-</span><span> Supported methods:
</span><span>  -</span><span> Mean
</span><span>  -</span><span> Median
</span><span>  -</span><span> Constant values
</span><span>-</span><span> Configurable per column

</span><span>### Duplicate Removal</span><span>
</span><span>-</span><span> Row-level duplicate elimination
</span><span>-</span><span> Deterministic behavior

</span><span>### Scaling Methods</span><span>
</span><span>-</span><span> Min-Max Scaling
</span><span>-</span><span> Z-Score Standardization
</span><span>-</span><span> Robust Scaling using Median and IQR

</span><span>### Outlier Handling (IQR-based)</span><span>
</span><span>-</span><span> Detection
</span><span>-</span><span> Value capping (winsorization)
</span><span>-</span><span> Row removal

</span><span>### Pipeline Execution</span><span>
</span><span>-</span><span> Sequential, configurable preprocessing steps
</span><span>-</span><span> Explicit execution flow inspired by sklearn pipelines

---

</span><span>## Installation</span><span>

```bash
pip install -r requirements.txt
</span></span></code></div></div></pre>

---

## Running the Demo

Run the end-to-end preprocessing pipeline from the repository root:

<pre class="overflow-visible! px-0!" data-start="1425" data-end="1451"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python demo.py
</span></span></code></div></div></pre>

The demo:

* Loads a small numeric dataset
* Applies a configurable preprocessing pipeline
* Prints raw and cleaned data for comparison

---

## Example Pipeline

<pre class="overflow-visible! px-0!" data-start="1615" data-end="1775"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>steps = [
    (</span><span>"fill_missing"</span><span>, {</span><span>"strategies"</span><span>: {</span><span>1</span><span>: </span><span>"median"</span><span>}}),
    (</span><span>"remove_duplicates"</span><span>, {}),
    (</span><span>"cap_outliers"</span><span>, {}),
    (</span><span>"robust_scale"</span><span>, {})
]
</span></span></code></div></div></pre>

---

## Design Decisions

* NumPy-only implementation to avoid abstraction leakage
* Column-wise logic to reflect real preprocessing requirements
* Explicit pipelines instead of hidden state
* Fail-fast validation on invalid input

---

## Known Limitations

* No categorical data support
* No automatic schema inference
* Less ergonomic than Pandas for real-world workflows

These limitations are intentional.

---

## When Not to Use This

* Production data pipelines
* Large-scale datasets
* Mixed-type tabular data
* Feature engineering for machine learning models

For these cases, Pandas and sklearn are more appropriate tools.

---

## Learning Outcome

This project serves as a foundation for understanding:

* Low-level preprocessing mechanics
* Tradeoffs between NumPy and Pandas
* How sklearn-style preprocessing pipelines are structured

The next planned step is to reimplement the same pipeline using Pandas and sklearn.
