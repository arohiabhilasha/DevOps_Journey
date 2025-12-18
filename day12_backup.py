import boto3
from botocore.exceptions import ClientError

# Set your region
region_name = 'ap-south-1'  # Change region if needed

# Initialize a session using boto3
session = boto3.Session(region_name=region_name)
ec2 = session.resource('ec2', region_name=region_name)
ec2_client = session.client('ec2', region_name=region_name)

# Prompt user for EC2 Instance ID
instance_id = input("Enter the EC2 Instance ID: ")

try:
    # Fetch the instance
    instance = ec2.Instance(instance_id)
    instance.load()  # Load instance attributes

    # Retrieve volume(s) attached to the instance
    volume_ids = [vol['Ebs']['VolumeId'] for vol in instance.block_device_mappings if 'Ebs' in vol]
    if not volume_ids:
        print(f"No EBS volumes attached to instance {instance_id}.")
        exit(1)

    # For demo, we'll use the first attached EBS volume
    volume_id = volume_ids[0]
    print(f"Volume ID attached to instance {instance_id}: {volume_id}")

    # Create a snapshot of the volume and tag it immediately
    description = f"Backup snapshot of {volume_id} from instance {instance_id}"

    # Prepare tags (list of dicts as per Boto3 style)
    tags = [
        {'Key': 'Name', 'Value': f"Backup-{volume_id}"},
        {'Key': 'CreatedBy', 'Value': 'day12_backup.py'},
        {'Key': 'InstanceId', 'Value': instance_id}
    ]

    # Create the snapshot and tag during creation
    response = ec2_client.create_snapshot(
        VolumeId=volume_id,
        Description=description,
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': tags
            }
        ]
    )

    snapshot_id = response['SnapshotId']
    print(f"Snapshot {snapshot_id} created successfully for volume {volume_id} and tagged.")

except ClientError as e:
    print(f"Failed: {e}")
except Exception as ex:
    print(f"Unexpected error: {ex}")

