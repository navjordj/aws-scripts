import sys
import csv

import boto3
from tqdm import tqdm

def iterate_bucket_items(client, bucket):
    paginator = client.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket)

    for page in page_iterator:
        if page['KeyCount'] > 0:
            for item in page['Contents']:
                yield item

if __name__ == "__main__":
    BUCKET_FROM = sys.argv[1]
    BUCKET_TO = sys.argv[2]
    CSV_FILE = sys.argv[3] 

    with open(CSV_FILE) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        files = [row[0] for row in csv_reader]

    s3 = boto3.client('s3')

    length = len(s3.list_objects(Bucket=BUCKET_FROM)["Contents"])

    dest = boto3.resource('s3').Bucket(BUCKET_TO)

    for item in tqdm(iterate_bucket_items(s3, BUCKET_FROM), total=length):
        if item["Key"] in files:
            dest.copy({'Bucket': BUCKET_FROM, 'Key': item["Key"]}, item["Key"])
