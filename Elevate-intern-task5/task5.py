# Full Code for Elevate Labs Task 5: Exploratory Data Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Load and Inspect Data ---

# Set pandas to display all columns
pd.set_option('display.max_columns', None)

# Load the dataset from the CSV file
df = pd.read_csv('train.csv')

print("--- Initial Data Head ---")
print(df.head())
print("\n" + "="*50 + "\n")

print("--- Data Structure and Info ---")
df.info()
print("\n" + "="*50 + "\n")

print("--- Initial Missing Values ---")
print(df.isnull().sum())
print("\n" + "="*50 + "\n")


# --- 2. Clean the Data ---

# Fill missing 'Age' values with the median age
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing 'Embarked' values with the mode (most frequent port)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop the 'Cabin' column due to excessive missing values
df.drop('Cabin', axis=1, inplace=True)

print("--- Missing Values After Cleaning ---")
print(df.isnull().sum())
print("\n" + "="*50 + "\n")


# --- 3. Visualize the Data and Save Plots ---

# Plot 1: Overall Survival Count
plt.figure(figsize=(6, 4))
sns.countplot(x='Survived', data=df)
plt.title('Overall Survival Count (0 = No, 1 = Yes)')
plt.savefig('plot01_overall_survival.png') # Save the plot
plt.show()

# Plot 2: Survival Count by Gender
plt.figure(figsize=(6, 4))
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival Count by Gender')
plt.savefig('plot02_survival_by_gender.png') # Save the plot
plt.show()

# Plot 3: Survival Count by Passenger Class
plt.figure(figsize=(6, 4))
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Survival Count by Passenger Class')
plt.savefig('plot03_survival_by_pclass.png') # Save the plot
plt.show()

# Plot 4: Age Distribution of Passengers
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution of Passengers')
plt.savefig('plot04_age_distribution.png') # Save the plot
plt.show()

# Plot 5: Correlation Heatmap
numeric_cols = df.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(10, 7))
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Numerical Features')
plt.savefig('plot05_correlation_heatmap.png') # Save the plot
plt.show()

print("All plots have been generated and saved as PNG files.")
print("Exploratory Data Analysis is complete!")

