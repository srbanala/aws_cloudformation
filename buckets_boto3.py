# To list buckets
import boto3
s3_client=boto3.client('s3')
response=s3_client.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])

# To create buckets

import logging
import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name,region=None):
    """Create an S3 bucket in a specified region

      If a region is not specified, the bucket is created in the S3 default
      region (us-east-1).

      :param bucket_name: Bucket to create
      :param region: String region to create bucket in, e.g., 'us-west-2'
      :return: True if bucket created, else False
      """
    try:
        if region is None:
            s3_client=boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client=boto3.client('s3',region_name=region)
            location={'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


#print(create_bucket('rtvks','us-east-2'))


## Ec2 instances
import boto3
ec2 = boto3.client('ec2','us-east-1')
response = ec2.describe_instances()
for instance in response['Reservations']:
    print('ImageID=',instance['Instances'][0]['ImageId'],'Instance-id=',instance['Instances'][0]['InstanceId'])

ec2=boto3.client('ec2','us-east-1')
response=ec2.describe_regions()
print('Regions:',response['Regions'])

response=ec2.describe_availability_zones()
print('Availabiility Zones:',response['AvailabilityZones'])

iam=boto3.client('iam')
paginator=iam.get_paginator('list_users')
for response in paginator.paginate():
    print(response)