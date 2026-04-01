import pandas as pd
from sqlalchemy import create_engine

DB_URI = "postgresql://user:password@localhost:5432/salary_db"

def extract():
    return pd.read_csv("data/employees.csv")

def transform(df):
    df.dropna(inplace=True)
    df['department'] = df['department'].str.upper()

    df['salary_category'] = df['salary'].apply(
        lambda x: 'HIGH' if x > 80000 else 'MEDIUM' if x > 50000 else 'LOW'
    )
    return df

def load(df):
    engine = create_engine(DB_URI)
    df.to_sql("employee_cleaned", engine, if_exists="replace", index=False)

def run_etl():
    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    run_etl()
