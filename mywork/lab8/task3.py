#!/usr/bin/env python3
import boto3
import logging
import sys
import glob

logging.basicConfig(level=logging.INFO)

def parse_args():
	input_folder = sys.argv[1]
	destination = sys.argv[2]
	return input_folder, destination

def upload(input_folder, destination):
	try:
		s3 = boto3.client('s3', region_name="us-east-1")
		bucket_name, prefix = destination.split("/", 1)
		search_pattern = f"{input_folder}/results*.csv"
		files = glob.glob(search_pattern)

		for local_file in files:
			csv_file = local_file.split("/")
			csv_file = csv_file[-1]
			key = f"{prefix}{csv_file}"

			with open(local_file, "rb") as f:
				s3.put_object(Bucket=bucket_name, Key=key, Body=f)
	except Exception as e:
		logging.error(f"Error occured: {e}")

def main():
	input_folder, destination = parse_args()
	upload(input_folder, destination)

if __name__ == "__main__":
	main()
