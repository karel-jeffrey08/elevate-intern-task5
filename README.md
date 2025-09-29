# Task 5: Exploratory Data Analysis (EDA) on the Titanic Dataset

This repository contains the project for Task 5 of the Elevate Labs Data Analyst Internship. It includes a comprehensive Exploratory Data Analysis (EDA) of the Titanic dataset, with the goal of identifying key factors that influenced passenger survival.

## Project Overview

The analysis follows a structured approach to explore the dataset:
- **Data Loading and Cleaning:** The `train.csv` dataset was loaded, inspected for inconsistencies, and cleaned to handle missing values.
- **Data Visualization and Analysis:** Various plots were generated using Python libraries (Pandas, Matplotlib, and Seaborn) to visualize relationships and derive insights from the data.
- **Reporting:** The findings are documented in both a Jupyter notebook and a final PDF report.

## Files in This Repository

This repository is organized with the following files:

- **`ElevateLabs_Task5_Titanic_EDA.ipynb`**: The primary Jupyter Notebook file with all the step-by-step code, markdown explanations, and generated outputs.
- **`ElevateLabs_Task5_Titanic_EDA_Report.pdf`**: A clean, exported PDF version of the final notebook for easy viewing.
- **`task5.py`**: A Python script containing the complete code to run the analysis and generate the plots.
- **`train.csv`**: The original Titanic dataset used for the analysis.
- **`TASK-5-Data-Analyst-ELEVATE-LABSs.pdf`**: The official task description and guidelines provided by Elevate Labs.

### Generated Plots

The `plots` folder contains all the visualizations generated during the analysis:
- **`plot01_overall_survival.jpg`**: A bar chart showing the overall count of passengers who survived versus those who did not.
- **`plot02_survival_by_gender.jpg`**: A bar chart illustrating the difference in survival rates between male and female passengers.
- **`plot03_survival_by_pclass.jpg`**: A bar chart comparing survival counts across the different passenger classes (1st, 2nd, and 3rd).
- **`plot04_age_distribution.jpg`**: A histogram showing the age distribution of the passengers.
- **`plot05_correlation_heatmap.jpg`**: A heatmap visualizing the correlation between the numerical features in the dataset.

## Summary of Key Findings

- **Survival Rate:** More passengers did not survive the disaster than those who did.
- **Gender Disparity:** Female passengers had a significantly higher rate of survival.
- **Class Impact:** Passengers in 1st class had the highest chances of survival, while 3rd class passengers had the lowest.
- **Age Demographics:** The majority of passengers were young adults, primarily between the ages of 20 and 40.

## How to Use

1.  **Clone the Repository:** Download all the files to your local machine.
2.  **Review the Notebook:** For a detailed walkthrough of the analysis, open the `ElevateLabs_Task5_Titanic_EDA.ipynb` file in a Jupyter or Google Colab environment.
3.  **Run the Script:** To reproduce the plots, you can execute the `task5.py` script. Ensure you have the required Python libraries installed (`pandas`, `matplotlib`, `seaborn`).
