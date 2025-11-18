import pandas as pd

df = pd.read_csv("sample_data.csv")

# Select only the required columns
df_clean = df[['age', 'bmi', 'blood_pressure', 'glucose']]

# Remove duplicate rows
df_clean = df_clean.drop_duplicates()

# Handle missing values
df_clean = df_clean.fillna(df_clean.mean())

# Reset the index
df_clean = df_clean.reset_index(drop=True)

# Save the cleaned dataset
df_clean.to_csv("cleaned_dataset.csv", index=False)