#!/usr/bin/python
import boto3
import argparse
import os
from requests_aws4auth import AWS4Auth

def listS3(event):
    #GET VARS FROM MAIN FUNTION
    bucket = event.get('bucket')
    prefix = event.get('prefix')
    client = boto3.client('s3', region_name=os.environ['AWS_REGION'])
    response = client.list_objects(Bucket=bucket, Prefix=prefix)
    
    for content in response.get('Contents', []) :
        if "GLACIER" in content.get('StorageClass'):
            print(content.get('Key'))
        else:
            print("not glacier storage found")

def main(argv):
    event = dict();
    event['bucket'] = argv.bucket
    event['prefix'] = argv.prefix

    listS3(event)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-b', '--bucket'
    )
    parser.add_argument(
        '-p', '--prefix'
    )
    args = parser.parse_args()
    main(args)
