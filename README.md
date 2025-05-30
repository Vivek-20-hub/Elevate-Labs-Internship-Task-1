# Elevate-Labs-Internship-Task-1
# People Data Cleaning and Preprocessing

This Task-1 focuses on cleaning and preprocessing the "people-1000.csv" dataset using Python and the pandas library. The goal is to prepare the dataset for further analysis by handling inconsistencies, standardizing data formats, and ensuring correct data types.

## Dataset

The dataset used in this task-1 is "people-1000.csv".

## Task

The primary task is to perform data cleaning and preprocessing on the "people-1000.csv" dataset. This involves:

- Identifying and handling missing values (although none were found in this specific dataset).
- Removing duplicate rows (although none were found in this specific dataset).
- Standardizing text values (e.g., gender).
- Converting date formats to a consistent type.
- Renaming column headers to be clean and uniform (lowercase, no spaces).
- Checking and fixing data types.

## Data Cleaning Steps

The following steps were taken to clean and preprocess the data:

1.  **Load Data**: The "people-1000.csv" file was loaded into a pandas DataFrame.
2.  **Standardize 'Sex' Column**: Variations in the 'Sex' column (like 'male', 'M', 'F') were standardized to 'Male' and 'Female'.
3.  **Standardize 'Job Title' Column**: A basic mapping was applied to standardize some job titles. This step can be expanded based on further data exploration.
4.  **Convert 'Date of birth' to Datetime**: The 'Date of birth' column was converted to datetime objects. Invalid date formats were coerced to `NaT` (Not a Time).
5.  **Rename Columns**: All column names were converted to lowercase and spaces were replaced with underscores.
6.  **Adjust Data Types**: The data type of the 'index' column was confirmed or adjusted to `int64`.

## Summary of Changes

- No missing values or duplicate rows were found or removed.
- The 'Sex' column was standardized.
- A basic standardization was applied to the 'Job Title' column.
- The 'Date of birth' column was converted to datetime objects.
- Column names were standardized to lowercase with underscores.
- The data type of the 'index' column was confirmed/adjusted.
