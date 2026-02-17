#!/usr/bin/env python
import requests
import json
import pandas as pd
import sys
import logging
import os
import time

URL =  "http://api.open-notify.org/iss-now.json"

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

def load(df, csv_file):
	"""Load: If CSV file exists, append dataframe as new line, else create CSV file with first line appended"""
	if os.path.exists(csv_file):
		original_df = pd.read_csv(csv_file)
		appended_df = pd.concat([original_df, df])
		logging.info("CSV file found, appended new line to file")
		return appended_df.to_csv(csv_file, index=False)
	else:
		logging.info("CSV file not found, created new CSV file with appended first line")
		return df.to_csv(csv_file, index=False)

def main():
	for i in range(10):
		csv_file = sys.argv[1]
		data = extract(URL)
		df = transform(data)
		load(df, csv_file)

		time.sleep(1)

if __name__ == "__main__":
	main()
