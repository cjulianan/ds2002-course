#!/usr/bin/env python3
import boto3
import sys

# create client
s3 = boto3.client('s3', region_name="us-east-1")

bucket = 'ds2002-fvd6wy'
local_file = 'cloud.jpg'
bucket_name = "ds2002-fvd6wy"
local_file = "cloud.jpg"
key = "cloud.jpg"

if len(sys.argv) > 1 and sys.argv[1] == "public-read":
	acl = "public-read"
	with open(local_file, "rb") as f:
		s3.put_object(Bucket=bucket_name, Key=key, Body=f, ACL=acl)

	print(s3.generate_presigned_url(ClientMethod="get_object", Params={"Bucket": bucket_name, "Key": key}, ExpiresIn=30))
else:
	with open(local_file, "rb") as f:
    		s3.put_object(Bucket=bucket_name, Key=key, Body=f)
