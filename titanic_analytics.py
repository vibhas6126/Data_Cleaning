import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("train.csv")

# Display first rows
print("\nFirst 5 rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Age with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill Embarked with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop Cabin column
df.drop(columns=['Cabin'], inplace=True)

# Check duplicates
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Data types
print("\nData Types:")
print(df.dtypes)

# ----------------------
# Outlier Removal (Age)
# ----------------------

Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR

df = df[(df['Age'] >= lower) & (df['Age'] <= upper)]

# Save cleaned data
df.to_csv("cleaned_titanic.csv", index=False)

print("\nCleaned Dataset Saved Successfully")

# Histogram of Age

plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=20, kde=True)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()

# Gender Distribution

plt.figure(figsize=(6,5))
sns.countplot(x='Sex', data=df)

plt.title("Gender Distribution")

plt.show()

# Survival Count

plt.figure(figsize=(6,5))
sns.countplot(x='Survived', data=df)

plt.title("Survival Count")

plt.show()

# Passenger Class Distribution

plt.figure(figsize=(6,5))
sns.countplot(x='Pclass', data=df)

plt.title("Passenger Class Distribution")

plt.show()

# Survival by Gender

plt.figure(figsize=(7,5))
sns.countplot(x='Sex', hue='Survived', data=df)

plt.title("Survival by Gender")

plt.show()

# Age Boxplot

plt.figure(figsize=(8,5))
sns.boxplot(x=df['Age'])

plt.title("Age Box Plot")

plt.show()

# Fare Boxplot

plt.figure(figsize=(8,5))
sns.boxplot(x=df['Fare'])

plt.title("Fare Box Plot")

plt.show()

# Correlation Heatmap

plt.figure(figsize=(10,8))

corr = df.corr(numeric_only=True)

sns.heatmap(corr,
            annot=True,
            cmap='coolwarm')

plt.title("Correlation Heatmap")

plt.show()

# Pair Plot

sns.pairplot(df[['Age', 'Fare', 'Pclass', 'Survived']],
             hue='Survived')

plt.show()

# Survival Percentage

df['Survived'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Survival Percentage")
plt.ylabel("")

plt.show()