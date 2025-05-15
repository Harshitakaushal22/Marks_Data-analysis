import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("E:\harshita\marks\student-mat.csv", sep=";")
print("First 5 Rows:\n", df.head())
print("\nMissing Values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)
print("\nDataset Shape:", df.shape)
df = df.drop_duplicates()
print("\nShape after removing duplicates:", df.shape)
# Average final grade
avg_g3 = df["G3"].mean()
print("\nAverage Final Grade (G3):", round(avg_g3, 2))
# Students scoring above 15
above_15 = df[df["G3"] > 15].shape[0]
print("Students scoring above 15 in G3:", above_15)
#  Correlation between studytime and G3
correlation = df["studytime"].corr(df["G3"])
print("Correlation between study time and G3:", round(correlation, 2))
# Average G3 by gender
avg_by_gender = df.groupby("sex")["G3"].mean()
print("\nAverage G3 by Gender:\n", avg_by_gender)
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
plt.hist(df["G3"], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Final Grades (G3)")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.grid(True)
plt.tight_layout()
plt.show()
# Scatter studytime vs G3
plt.figure(figsize=(8, 5))
sns.scatterplot(x="studytime", y="G3", data=df, hue="sex")
plt.title("Study Time vs Final Grade (G3)")
plt.xlabel("Study Time (hours)")
plt.ylabel("Final Grade (G3)")
plt.tight_layout()
plt.show()
#  Bar chart: average G3 by gender
plt.figure(figsize=(6, 4))
sns.barplot(x=avg_by_gender.index, y=avg_by_gender.values, palette="pastel")
plt.title("Average Final Grade by Gender")
plt.xlabel("Gender")
plt.ylabel("Average G3")
plt.tight_layout()
plt.show()