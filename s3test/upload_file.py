from variables import *

import boto3

s3 = boto3.resource('s3')

data = open('katt.jpeg', 'rb')
s3.Bucket(bucket1).put_object(Key='katt.jpeg', Body=data)
print("suksess?")