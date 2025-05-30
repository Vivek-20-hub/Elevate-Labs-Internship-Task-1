import pandas as pd

try:
    df = pd.read_csv('people-1000.csv')
except FileNotFoundError:
    print("Error: 'people-1000.csv' not found. Please ensure the file exists in the current directory.")
    exit() 
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

df['Sex'] = df['Sex'].replace({'male': 'Male', 'M': 'Male', 'F': 'Female'})

job_title_mapping = {
    'Software Engineer': ['Software Engineer', 'Software Developer', 'Sr. Software Engineer', 'Lead Software Engineer'],
  
}

def standardize_job_title(job_title):
    if pd.isna(job_title): 
        return job_title
    for standard_title, variations in job_title_mapping.items():
        if job_title in variations:
            return standard_title
    return job_title

df['Job Title'] = df['Job Title'].apply(standardize_job_title)
df['Date of birth'] = pd.to_datetime(df['Date of birth'], errors='coerce')
df.columns = [col.lower().replace(' ', '_') for col in df.columns]


if 'index' in df.columns:
    if df['index'].dtype != 'int64':
        df['index'] = df['index'].astype('int64')

display(df.head())
print(df.dtypes)


df.to_csv('cleaned_people_data.csv', index=False)
