#!/usr/bin/python
import boto.ec2
print("To Terminate EC2 Instance Please Enter The Below Details!!!")
region=raw_input("Enter Your EC2 Region: ")
conn = boto.ec2.connect_to_region(region)
ec2_id=raw_input("Enter Your EC2 instance ID: ")
conn.terminate_instances(instance_ids=[ec2_id])
