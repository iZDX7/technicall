import pandas as pd

df = pd.read_csv('day12_users.csv')

def standardize_city(df):
    df['city'] = df['city'].str.strip().str.lower().str.replace(r'[^\w\s]', '', regex=True)
    synonyms = {'nyc': 'new york', 'san francisco': 'san francisco'}
    df['city'] = df['city'].replace(synonyms)
    return df

def parse_and_localize(df):
    df['signup_time'] = pd.to_datetime(df['signup_time'], errors='coerce', utc=True)
    return df

df = standardize_city(df)
df = parse_and_localize(df)
print(df[['city', 'signup_time']])
