import os
import logging
import mysql.connector
import pandas as pd
from mysql.connector import Error
logger = logging.getLogger(__name__)
DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")
def read_data(filename):
    """Takes a csv file and returns a pandas dataframe"""
    df = pd.read_csv(filename)
    logger.info(
        "Reading file: %s has been fed into a dataframe", filename,
    )
    return df
def clean_data(data):
    """Removes rows with missing values"""
    rows_before = len(data)
    df_clean = data
    df_clean = df_clean.dropna()
    rows_after = len(df_clean)
    logger.info(
        "Cleaning data: dropped %s rows with missing values; %s rows remain",
        rows_before - rows_after,
        rows_after,
    )
    return df_clean
def load_data(data, table='mock'):
    """Writes a dataframe to MySQL"""
    type_mapping = {
        "int64": "BIGINT",
        "int32": "INT",
        "float64": "DOUBLE",
        "bool": "TINYINT(1)",
        "datetime64[ns]": "DATETIME",
        "object": "VARCHAR(255)",
        "str": "VARCHAR(255)",
    }
    sql_types = {
        col: type_mapping[str(dtype)]
        for col, dtype in data.dtypes.items()
    }
    col_defs = ", ".join(
        f"`{col}` {sql_type}"
        for col, sql_type in sql_types.items()
    )
    create_sql = f"CREATE TABLE IF NOT EXISTS `{table}` ({col_defs})"
    cols = ", ".join(f"`{c}`" for c in data.columns)
    placeholders = ", ".join(["%s"] * len(data.columns))
    insert_sql = f"INSERT INTO `{table}` ({cols}) VALUES ({placeholders})"
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME
        )
        cursor = conn.cursor()
        cursor.execute(create_sql)
        for row in data.itertuples(index=False, name=None):
            cursor.execute(insert_sql, tuple(row))
        conn.commit()
        logger.info("Loaded %s rows into %s.%s", len(data), DBNAME, table)
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        logger.exception("Failed to load data into %s", table)
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
def main(file):
	"""Executes all functions"""
	df = read_data(file)
	clean = clean_data(df)
	load_data(clean)
if __name__ == "__main__":
	main("MOCK_DATA.csv")
