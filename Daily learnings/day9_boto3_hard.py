import boto3 
import os 
import time
from botocore.exceptions import ClientError

session = boto3.Session()
client_s3 = session.client('s3')

buckets = client_s3.list_buckets()
for bucket in buckets['Buckets']:
    print(f"Bucket: {bucket['Name']}")

#Ask user for bucket input
bucket_new = input("Enter the bucket name you want to create: ")

try:
    #Create the bucket (use create_bucket, not create)
    # Note: Bucket names must be globally unique and follow S3 naming rules
    print(f"Creating bucket: {bucket_new}...")
    client_s3.create_bucket(Bucket=bucket_new, CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
    print(f"Bucket {bucket_new} created successfully!")
    
    #Add a dummy text file to the bucket
    print(f"Uploading file: server.log to bucket: {bucket_new}...")
    client_s3.upload_file('DevOps_Journey/server.log', bucket_new, 'dummy.txt')
    print(f"File uploaded successfully!")
    
    #Add sleep time for 30 seconds
    print("Waiting 30 seconds before listing objects...")
    time.sleep(30)
    
    #List the files from the bucket
    print(f"Listing files in bucket: {bucket_new}...")
    response = client_s3.list_objects_v2(Bucket=bucket_new)
    if 'Contents' in response:
        print(f"Files in bucket {bucket_new}:")
        for obj in response['Contents']:
            print(f"  - {obj['Key']}")
    else:
        print(f"No files found in bucket {bucket_new}")
    
    print(f"\nWaiting 30 seconds before deleting...")
    time.sleep(30)
    
    #Delete the object first (bucket must be empty to delete)
    print(f"Deleting object 'dummy.txt' from bucket: {bucket_new}...")
    client_s3.delete_object(Bucket=bucket_new, Key='dummy.txt')
    print("Object deleted successfully!")
    
    #Delete the bucket (must be empty)
    print(f"Deleting bucket: {bucket_new}...")
    client_s3.delete_bucket(Bucket=bucket_new)
    print(f'Bucket {bucket_new} deleted successfully!')
    
except ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == 'BucketAlreadyExists':
        print(f"Error: Bucket '{bucket_new}' already exists. Bucket names must be globally unique.")
    elif error_code == 'BucketAlreadyOwnedByYou':
        print(f"Error: You already own bucket '{bucket_new}'.")
    else:
        print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")

