import os
import yaml
import pandas as pd
import sqlite3

from src.ui import build_app

# === Load API Keys ===
with open("config/api_keys.yaml") as f:
    api_keys = yaml.safe_load(f)

# === Load ETF dataset into SQLite ===
data_path = "data/etf_dataset_sample.csv"
db_file = "etf_database.db"
df = pd.read_csv(data_path)
conn = sqlite3.connect(db_file)
df.to_sql("etf_prices", conn, if_exists="replace", index=False)
conn.close()

# === Extract schema for prompting ===
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(etf_prices)")
columns = cursor.fetchall()
schema = ", ".join([f"{col[1]} ({col[2]})" for col in columns])
conn.close()

# === Launch Gradio App ===
demo = build_app(schema, db_file, api_keys)
demo.launch()
