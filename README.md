# Task 5: Exploratory Data Analysis (EDA) on the Titanic Dataset

This repository contains the project for Task 5 of the Elevate Labs Data Analyst Internship. The project focuses on performing a comprehensive Exploratory Data Analysis on the classic Titanic dataset.

## Project Overview

The objective of this analysis is to explore the Titanic passenger data to identify key factors that influenced survival rates. The project involves several stages:
- **Data Loading and Inspection:** Understanding the structure and content of the dataset.
- **Data Cleaning:** Handling missing values in columns like 'Age' and 'Embarked', and dropping columns with insufficient data like 'Cabin'.
- **Data Visualization:** Creating various plots (bar charts, histograms, and a heatmap) to visualize relationships between different variables.
- **Insight Generation:** Drawing conclusions based on the visualizations.

The analysis was conducted using Python with the Pandas, Matplotlib, and Seaborn libraries in a Google Colab notebook.

## Key Findings

- **Overall Survival:** A significant majority of the passengers in this dataset did not survive the tragedy.
- **Survival by Gender:** Female passengers had a markedly higher chance of survival compared to male passengers, aligning with the "women and children first" historical protocol.
- **Survival by Class:** A passenger's socio-economic status, represented by their ticket class (`Pclass`), was a strong predictor of survival. 1st class passengers had the highest survival rate, while 3rd class passengers had the lowest.
- **Age Distribution:** The passenger list was diverse in age, but the largest demographic consisted of young adults between the ages of 20 and 40.

## Files in this Repository

- `ElevateLabs_Task5_Titanic_EDA.ipynb`: The main Jupyter/Google Colab notebook file containing all Python code, analysis, and outputs.
- `ElevateLabs_Task5_Titanic_EDA_Report.pdf`: A PDF version of the notebook for easy viewing and accessibility.
- `train.csv`: The raw dataset used for this analysis.
- `my_learnings.md`: A document outlining the personal learnings and skills gained from this task.
- `README.md`: This file, providing an overview of the project.

## How to Use

1.  Clone this repository or download the files.
2.  Ensure you have Python and the required libraries (Pandas, Matplotlib, Seaborn) installed.
3.  Open the `ElevateLabs_Task5_Titanic_EDA.ipynb` file in a Jupyter Notebook or Google Colab environment.
4.  You can run the cells sequentially to reproduce the analysis and see the results.
