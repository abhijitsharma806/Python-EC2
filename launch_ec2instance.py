#!/usr/bin/python
import boto.ec2
print("To Launch EC2 Instance Please Enter The Below Details!!!")
region=raw_input("Enter Your EC2 Region: ")
conn = boto.ec2.connect_to_region(region)
ec2_ami_id=raw_input("Enter Your EC2 Image ID: ")
ec2_key_name=raw_input("Enter Your EC2 Key Name: ")
ec2_min=raw_input("Enter Your Minimum Required EC2: ")
ec2_max=raw_input("Enter Your Maximum required EC2: ")
ec2_type=raw_input("Enter Your EC2 Type: ")
ec2_security_group=raw_input("Enter Your EC2 SecurityGroup: ")
conn.run_instances(ec2_ami_id,key_name=ec2_key_name,min_count=ec2_min,max_count=ec2_max,instance_type=ec2_type,security_groups=[ec2_security_group])
