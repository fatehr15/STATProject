import pandas as pd

df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    "London":[5,6,9,11,15,18,20,20,17,13,9,6],
    "Paris":[4,5,9,12,16,19,22,22,18,14,9,6],
    "Rome":[8,10,13,16,20,25,28,28,24,19,14,10]
})
df.to_csv("data/temperatures.csv", index=False)
