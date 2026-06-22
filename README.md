# Titanic Dataset Data Cleaning and Exploratory Data Analysis

## Overview

This project demonstrates data preprocessing and exploratory data analysis (EDA) using the Titanic dataset. The project uses Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn to clean the dataset and prepare it for analysis.

## Tools and Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Dataset Information

- Total records: 891
- Total columns: 12

### Columns

- PassengerId
- Survived
- Pclass
- Name
- Sex
- Age
- SibSp
- Parch
- Ticket
- Fare
- Cabin
- Embarked

## Missing Values Detected

| Column | Missing Values |
|----------|---------------|
| Age | 177 |
| Cabin | 687 |
| Embarked | 2 |

## Data Cleaning Performed

### Handling Missing Values

- Missing values in the **Age** column were replaced with the median age.
- Missing values in the **Embarked** column were replaced with the mode.
- The **Cabin** column was removed due to a large number of missing values.

### Duplicate Removal

- Duplicate rows were checked.
- No duplicate records were found.

### Outlier Treatment

- Outliers in the **Age** column were detected and removed using the Interquartile Range (IQR) method.

### Dataset Export

- The cleaned dataset was saved as:

```
cleaned_titanic.csv
```

## Project Structure

```
Task 1
│
├── train.csv
├── cleaned_titanic.csv
└── titanic_analytics.py
```

## Python Code Features

- Dataset loading
- Dataset information display
- Missing value detection
- Missing value treatment
- Duplicate record detection
- Outlier removal using IQR
- Exporting cleaned data to CSV

## Output

The program displays:

- First five rows of the dataset
- Dataset information
- Missing values summary
- Duplicate row count
- Data types of each column
- Confirmation message after saving the cleaned dataset

## Author

Vibhas Chowdhary
