import boto3
from flask import Flask, render_template, request
from pymysql import *
import os
import boto3
from config import *

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "<dataemployee001>"


def upload_file(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response

def show_image(bucket):
    s3_client = boto3.client('s3')
    public_urls = ["https://s3{0}.amazonaws.com/{1}/{2}"]
    try:
        for item in s3_client.list_objects(Bucket=bucket)['Contents']:
            presigned_url = s3_client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': item['Key']}, ExpiresIn = 100)
            public_urls.append(presigned_url)
    except Exception as e:
        pass
    # print("[INFO] : The contents inside show_image = ", public_urls)
    return public_urls
