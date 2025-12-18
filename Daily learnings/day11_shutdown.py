import boto3
from botocore.exceptions import ClientError

session = boto3.Session(region_name='ap-south-1')
ec2_resource = session.resource('ec2')

for instance in ec2_resource.instances.all():
    # instance.tags is a list, not a dict, so we need to iterate or convert it
    # Convert tags list to dictionary for easier access
    tags_dict = {}
    if instance.tags:
        tags_dict = {tag['Key']: tag['Value'] for tag in instance.tags}
    
    # Now we can use .get() on the dictionary
    if tags_dict.get('Environment') == 'Dev':
        try:
            instance.stop()
            print(f"Stopped instance: {instance.id}")
        except ClientError as e:
            print(f"Error stopping instance {instance.id}: {e}")
    else:
        print(f"Skipping instance: {instance.id} (Environment: {tags_dict.get('Environment', 'N/A')})")

print("All Dev instances stopped")