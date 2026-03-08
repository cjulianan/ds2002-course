#!/usr/bin/env python3
from pymongo import MongoClient, errors
import os

def main():
	uri = os.getenv('MONGODB_ATLAS_URL')
	username = os.getenv('MONGODB_ATLAS_USER')
	password = os.getenv('MONGODB_ATLAS_PWD')

	client = MongoClient(uri, username=username, password=password, connectTimeoutMS=200, retryWrites=True)
	db = client.bookstore
	collection = db.authors

	document_count = collection.count_documents({})
	print(f"There are a total of {document_count} documents in the authors collection")

	authors = collection.find({})
	for author in authors:
		print(f"Name: {author['name']}, Nationality: {author['nationality']}")

	client.close()

if __name__ == "__main__":
	main()
