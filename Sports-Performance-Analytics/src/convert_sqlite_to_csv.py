import sqlite3
import pandas as pd
from pathlib import Path

# Paths
RAW_DIR = Path("data/raw")
DB_PATH = RAW_DIR / "database.sqlite"   # change name if needed
OUTPUT_DIR = RAW_DIR

# Connect to SQLite
conn = sqlite3.connect(DB_PATH)

# Get all table names
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
table_names = tables["name"].tolist()

print("Tables found:", table_names)

# Export each table to CSV
for table in table_names:
    print(f"Exporting {table}...")
    df = pd.read_sql_query(f"SELECT * FROM {table};", conn)
    df.to_csv(OUTPUT_DIR / f"{table}.csv", index=False)

conn.close()

print("All tables exported successfully!")
