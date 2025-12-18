import boto3
from botocore.exceptions import ClientError

session = boto3.Session(region_name='ap-south-1')

ec2_resource = boto3.resource('ec2', region_name='ap-south-1')

running_count = 0
stopped_count = 0
running_instance_type = []

print("Listing EC2 instances in ap-south-1:")
for instance in ec2_resource.instances.all():
    state = instance.state['Name']
    print(f"Instance ID: {instance.id}, State: {state}")
    if state == 'running':
        running_count += 1
        running_instance_type.append(instance.instance_type)
    elif state == 'stopped':
        stopped_count += 1

print(f"\nTotal running instances: {running_count}")
print(f"Total stopped instances: {stopped_count}")

if running_count > 0:
    print("COST WARNING: There are servers running in ap-south-1. You may incur charges.")
    print(f"Running instance types: {running_instance_type}")

