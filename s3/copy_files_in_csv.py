from helper_function import iterate_bucket_items
from variables import *

import pandas as pd

import boto3
from tqdm import tqdm


files: pd.DataFrame = pd.read_csv('data/files.csv')

files: pd.Series = files.iloc[:, 0]
print(files[0])
print('00001ade-2d63-4d5a-bec6-0330144cceda.h5' in list(files))

s3 = boto3.client('s3')

length = len(s3.list_objects(Bucket=bucket1)["Contents"])
print(length)

dest = boto3.resource('s3').Bucket(bucket2)

for item in tqdm(iterate_bucket_items(s3, bucket1), total=length):
    print(type(item["Key"]))
    print(type(files[0]))
    if item["Key"] in files:
        print(f'{item["Key"]} in csv')
        #dest.copy({'Bucket': bucket1, 'Key': item["Key"]}, item["Key"])
    else:
        print(f'{item["Key"]} not in csv')