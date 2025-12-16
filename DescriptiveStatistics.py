import numpy as np
from scipy import stats
import pandas as pd

df = pd.read_csv("data/temperatures.csv")

def summary(arr):
    arr = np.array(arr, dtype=float)
    return {
        "mean": arr.mean(),
        "median": np.median(arr),
        "mode": stats.mode(arr, keepdims=True).mode.tolist(),
        "range": arr.max()-arr.min(),
        "variance": arr.var(ddof=0),
        "std": arr.std(ddof=0),
        "Q1": np.percentile(arr,25),
        "Q3": np.percentile(arr,75),
        "IQR": np.percentile(arr,75)-np.percentile(arr,25)
    }

for city in ["London","Paris","Rome"]:
    print(city, summary(df[city].values))

