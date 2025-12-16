import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/temperatures.csv")

# ---------- 1) Line Chart ----------
plt.figure()
for city in ["London", "Paris", "Rome"]:
    plt.plot(df["Month"], df[city], marker="o", label=city)

plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.title("Monthly Temperature Trends")
plt.legend()
plt.grid(True)
plt.savefig("figs/line_trends.png", bbox_inches="tight")
plt.close()

# ---------- 2) Box Plot ----------
plt.figure()
sns.boxplot(data=df[["London", "Paris", "Rome"]])
plt.ylabel("Temperature (°C)")
plt.title("Boxplot of Monthly Temperatures")
plt.savefig("figs/boxplot.png", bbox_inches="tight")
plt.close()

# ---------- 3) Histogram (London) ----------
plt.figure()
plt.hist(df["London"], bins=6, edgecolor="black")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.title("Histogram of London Monthly Temperatures")
plt.savefig("figs/histogram_london.png", bbox_inches="tight")
plt.close()

# ---------- 4) Violin Plot ----------
plt.figure()
sns.violinplot(data=df[["London", "Paris", "Rome"]])
plt.ylabel("Temperature (°C)")
plt.title("Violin Plot of Monthly Temperatures")
plt.savefig("figs/violin.png", bbox_inches="tight")
plt.close()

print("All visualizations saved in the figs/ directory")
