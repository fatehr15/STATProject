## Project title
Monthly Temperature Analysis for London, Paris, and Rome


**Delivered to:** Alaeddine RAKI

**Email:** alaeddine.raki@enscs.edu.dz
---

## Project summary
In this project, I analyzed monthly temperature data for three European cities: London, Paris, and Rome. I focused on computing descriptive statistics, visualizing seasonal patterns and distributions, and interpreting the results from a statistical perspective. The entire workflow was designed to be reproducible and suitable for academic submission.

The main outputs of the project include:
- A cleaned dataset (`data/temperatures.csv`).
- Python scripts for data processing, statistical analysis, and visualization.
- Automatically generated figures illustrating trends and distributions.
- A table of descriptive statistics saved as a CSV file.
- A written statistical interpretation in Markdown format.

---

## Objectives
The objectives of this project were:
1. To compute measures of central tendency and dispersion (mean, median, mode, variance, standard deviation, and interquartile range) for each city.
2. To visualize monthly temperature trends and compare distributions across cities.
3. To analyze skewness, variability, and distributional shape using both numerical measures and graphical tools.
4. To produce a fully reproducible analysis using Python scripts and documented outputs.

---

## Project structure

```
.
├── data
│   └── temperatures.csv
├── DescriptiveStatistics.py
├── figs
│   ├── boxplot.png
│   ├── histogram_london.png
│   ├── line_trends.png
│   └── violin.png
├── importDATA.py
├── notebooks
│   └── analysis.ipynb
├── output
│   └── descriptive_statistics.csv
├── report.md
├── requirements.txt
├── StatisticalInterpretation
│   └── SI.md
└── Visualizations.py

6 directories, 13 files
```

---

## Methodology
I first organized the project structure and prepared the dataset in CSV format. I then used Python and scientific libraries to compute descriptive statistics for each city. These statistics were saved automatically to a CSV file to avoid manual transcription errors.

Next, I generated four visualizations: a line chart to show seasonal trends, a boxplot to compare variability, a histogram to analyze distribution shape, and a violin plot to visualize density and spread. Each figure was saved as an image file and later used for interpretation.

Finally, I analyzed the numerical results and plots together to draw statistically justified conclusions about skewness, variability, and normality.

---

## Reproducibility
I ensured that the entire analysis can be reproduced by running the provided Python scripts in sequence:

```bash
python3 importDATA.py
python3 DescriptiveStatistics.py
python3 Visualizations.py
```

All required dependencies are listed in `requirements.txt`, and the analysis notebook (`notebooks/analysis.ipynb`) can be used to rerun or explore the computations interactively.

---

## Results (summary)
From the analysis, I found that Rome has the highest average monthly temperature and the greatest variability. London shows the most consistent temperatures and is the closest to a normal distribution, while Paris lies between the two in terms of both average temperature and variability. All three cities exhibit slight positive skewness due to higher summer temperatures.

Detailed numerical results are available in `output/descriptive_statistics.csv`, and all visual evidence is provided in the `figs/` directory.

---

## Conclusion
Through this project, I demonstrated how descriptive statistics and visualization techniques can be combined to analyze and compare climate data. The use of reproducible code and automatically generated outputs ensures accuracy and transparency, while the interpretations link statistical measures directly to real-world seasonal behavior.

---

