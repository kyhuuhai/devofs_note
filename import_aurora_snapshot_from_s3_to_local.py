import os
import psycopg2
import json
import pandas as pd
import pyarrow.parquet as pq
import numpy as np

conn = psycopg2.connect(
    dbname="myapp_development",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"  # or whatever port you're using
)
cur = conn.cursor()

def safe_convert(value):
    if pd.isna(value):
        return None
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    return value

snapshot_dir = '.'
for table_dir in os.listdir(snapshot_dir):
    table_path = os.path.join(snapshot_dir, table_dir)
    if os.path.isdir(table_path):
        table_name = table_dir.split('.')[-1]  # Assumes format like 'public.races'
        print(f"Processing table: {table_name}")
        
        # Look for numbered subdirectories
        for subdir in os.listdir(table_path):
            subdir_path = os.path.join(table_path, subdir)
            if os.path.isdir(subdir_path) and subdir.isdigit():
                print(f"Processing subdirectory: {subdir}")
                
                for file in os.listdir(subdir_path):
                    if file.endswith('.parquet'):
                        file_path = os.path.join(subdir_path, file)
                        print(f"Importing file: {file}")
                        
                        # Read the Parquet file
                        df = pd.read_parquet(file_path)
                        
                        # Generate the SQL insert statement
                        columns = ', '.join(df.columns)
                        placeholders = ', '.join(['%s'] * len(df.columns))
                        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                        print(insert_query)
                        # Convert DataFrame to list of tuples for insertion, with type conversion
                        data = [tuple(safe_convert(x) for x in row) for row in df.itertuples(index=False, name=None)]
                        
                        # Execute the insert
                        try:
                            cur.executemany(insert_query, data)
                            print(f"Inserted {len(data)} rows into {table_name}")
                        except psycopg2.Error as e:
                            print(f"Error inserting data into {table_name}: {e}")
                            conn.rollback()  # Rollback the transaction on error
                            continue  # Move to the next file

conn.commit()
cur.close()
conn.close()
print("Success")
