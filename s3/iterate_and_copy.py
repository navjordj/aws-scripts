from helper_function import iterate_bucket_items
from variables import *

import boto3
from tqdm import tqdm


s3 = boto3.client('s3')

length = len(s3.list_objects(Bucket=bucket1)["Contents"])
print(length)

dest = boto3.resource('s3').Bucket(bucket2)

for item in tqdm(iterate_bucket_items(s3, bucket1), total=length):
    print(item)
    dest.copy({'Bucket': bucket1, 'Key': item["Key"]}, item["Key"])
