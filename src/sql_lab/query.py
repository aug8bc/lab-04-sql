#!/usr/bin/env python3

import json
import os

import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd

DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DBNAME)
cur = db.cursor()

def get_data_by_group(value):
	"""Selects all the rows that are in the Avengers group"""
	query = "SELECT * FROM mock WHERE `group` = %s;"
	try:
        	cur.execute(query, (value,))
        	results = cur.fetchall()
        	output = []
        	for r in results:
            		output.append(r)
        	return output
	except mysql.connector.Error as e:
        	print("MySQL Error: ", str(e))
        	return None
def plot_counts(groupby):
	"""Takes a column name and counts rows per distinct value of the column"""
	query = f"SELECT `{groupby}`, COUNT(`{groupby}`) FROM mock GROUP BY `{groupby}`;"
	try:
        	cur.execute(query)
        	results = cur.fetchall()
        	output = []
        	for r in results:
            		output.append(r)
        	df = pd.DataFrame(output)
        	df.plot.bar(x=0, y=1)
        	plt.tight_layout()
        	plt.show()
        	return df
	except mysql.connector.Error as e:
        	print("MySQL Error: ", str(e))
        	return None
def main():
	"""Runs everything and closes connection"""
	get_data_by_group('The Avengers')
	plot_counts('group')
	cur.close()
	db.close()
if __name__ == "__main__":
    main()
