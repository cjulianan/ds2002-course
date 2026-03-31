#!/bin/bash

AMI="ami-04680790a315cd58d"
INSTANCE_TYPE="t2.nano"
INSTANCE_NAME="ds2002-fvd6wy"
KEY_NAME="key-ec2"
SECURITY_GROUP_ID="sg-0be6679b34372f15a"
SUBNET_ID="subnet-085a38474f2e3b60c"

# Complete this command with the right flags (e.g. --image-id, --instance-type, --key-name,
# --security-group-ids, --subnet-id) and a Name tag from INSTANCE_NAME.
aws ec2 run-instances --image-id "$AMI" --instance-type "$INSTANCE_TYPE" --key-name "$KEY_NAME" --security-group-ids "$SECURITY_GROUP_ID" --subnet-id "$SUBNET_ID" --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$INSTANCE_NAME}]"
