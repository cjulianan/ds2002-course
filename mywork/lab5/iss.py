#!/usr/bin/env python
import requests
import json
import pandas as pd
import sys
import logging
import os
import time
import mysql.connector
from datetime import datetime

# db config stuff
DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DB = "iss"

URL =  "http://api.open-notify.org/iss-now.json"

def register_reporter(table, reporter_id, reporter_name):
	"""Checks if reporter_id is in reporter table. If not, inserts reporter_id and reporter_name into it"""
	db = mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DB)
	cursor = db.cursor(dictionary=True)

	try:
		query = f"SELECT reporter_id FROM {table} WHERE reporter_id = %s"
		cursor.execute(query, (reporter_id,))
		result = cursor.fetchone()

		if result:
			logging.info("reporter_id exists in reporter table")
		else:
			query = "INSERT INTO reporters (reporter_id, reporter_name) VALUES (%s, %s)"
			record_data = (reporter_id, reporter_name)
			cursor.execute(query, record_data)
			db.commit()
	except Exception as e:
		logging.error("An unexpected error occurred:", e)
	finally:
		cursor.close()
		db.close()

def parse_args():
	"""Parses 1 argument and returns it, gives error message if it fails"""
	try:
		csv_file = sys.argv[1]
	except IndexError:
		logging.error(f"Usage: python {sys.argv[0]} <csv_file>")
		sys.exit(1)
	return csv_file

def extract(url):
	"""Extract: Gets JSON file from API and returns it parsed"""
	logging.info(f"Getting data from {url}")

	try:
		response = requests.get(url)
		response.raise_for_status() # raise an exception for HTTP errors
		data = response.json()
		return data
	except requests.exceptions.HTTPError as e:
		logging.error("HTTP error occurred:", e)
	except requests.exceptions.RequestException as e:
		logging.error("A request error occurred:", e)
	except Exception as e:
		logging.error("An unexpected error occurred:", e)

def transform(data):
	"""Transform: Flatten data, convert timestamp to readable format, and return cleaned data"""
	logging.info("Flattening nested structure...")
	df = pd.json_normalize([data])
	df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
	df_clean = df.reset_index(drop=True)
	logging.info(f"Transformed: {df_clean.shape[0]} rows x {df_clean.shape[1]} columns")

	return df_clean

def load(data, reporter_id):
	"""Uses data returned by extract func and inserts into reporters table"""
	db = mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DB)
	cursor = db.cursor(dictionary=True)

	message = data["message"]
	timestamp = data["timestamp"]
	timestamp = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
	latitude = data["iss_position"]["latitude"]
	longitude = data["iss_position"]["longitude"]

	try:
		query = "INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id) VALUES (%s, %s, %s, %s, %s)"
		cursor.execute(query, (message, latitude, longitude, timestamp, reporter_id))
		db.commit()
	except Exception as e:
		logging.error("An unexpected error occurred:", e)
	finally:
		cursor.close()
		db.close()

def main():
	register_reporter("reporters", "fvd6wy", "Sherlock Chen")

	for i in range(10):
		data = extract(URL)
		load(data, "fvd6wy")
		time.sleep(1)

if __name__ == "__main__":
	main()
