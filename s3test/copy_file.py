from variables import *

import boto3

FILENAME = 'katt.jpeg'

s3 = boto3.resource('s3')
source= { 'Bucket' : bucket1, 'Key': FILENAME}
dest = s3.Bucket(bucket2)
dest.copy(source, FILENAME)
