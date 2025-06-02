
import pandas as pd

df = pd.read_csv('marketing_campaign.csv', sep='\t')
df_cleaned = df.drop_duplicates()
df_cleaned = df_cleaned.dropna()
df_cleaned.columns = df_cleaned.columns.str.strip().str.lower().str.replace(' ', '_')
text_columns = ['education', 'marital_status']
for col in text_columns:
    df_cleaned[col] = df_cleaned[col].str.title()
df_cleaned['dt_customer'] = pd.to_datetime(df_cleaned['dt_customer'], errors='coerce')
df_cleaned['income'] = pd.to_numeric(df_cleaned['income'], errors='coerce')
df_cleaned.to_csv('cleaned_marketing_campaign.csv', index=False)
