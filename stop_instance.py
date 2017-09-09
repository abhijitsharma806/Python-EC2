#!/usr/bin/python
import boto.ec2
print("To Stop EC2 Instance Please Enter The Below Details!!!")
region=raw_input("Enter Your EC2 Region: ")
ec2_id=raw_input("Enter Your EC2 instance ID: ")
conn = boto.ec2.connect_to_region(region)
conn.stop_instances(instance_ids=[ec2_id])
