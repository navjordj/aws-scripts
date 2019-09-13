from helper_function import iterate_bucket_items
from variables import *

import csv

import boto3
from tqdm import tqdm

FILE = 'data/files.csv'

files = open(FILE)

files = csv.reader(files)
files_list = []
for row in files:
    files_list.append(row[0])

s3 = boto3.client('s3')

length = len(s3.list_objects(Bucket=bucket1)["Contents"])
print(length)

dest = boto3.resource('s3').Bucket(bucket2)

for item in tqdm(iterate_bucket_items(s3, bucket1), total=length):
    if item["Key"] in files_list:
        dest.copy({'Bucket': bucket1, 'Key': item["Key"]}, item["Key"])