import pandas as pd
import time

def clean_chunk(df):
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['income'] = pd.to_numeric(df['income'], errors='coerce')
    df['city'] = df['city'].str.strip()
    return df

def process_large_file(path_in, path_out, chunksize):
    start = time.time()
    for i, chunk in enumerate(pd.read_csv(path_in, chunksize=chunksize)):
        cleaned = clean_chunk(chunk)
        cleaned.to_csv(path_out, mode='a' if i else 'w', header=not i, index=False)
    print(f"Time: {time.time() - start} seconds")
