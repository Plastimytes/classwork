import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

from pathlib import Path

#Load dataset
# Get directory containing this script
script_dir = Path(__file__).resolve().parent

# Load dataset using absolute path built dynamically
# Load dataset using absolute path
df = pd.read_csv(r"C:\Users\Richard\Desktop\Year 3\Semester 1\Data Informatics\Week 2\PreOwned_Cars\pre-ownedcars.csv")


#Display firrst 5 rows
print(df.head())
print("------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------------")


#Data types and missing values
print(df.info())
print("------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------------")


print(df['brand'].value_counts())
print("------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------------")
print(df['model'].value_counts())