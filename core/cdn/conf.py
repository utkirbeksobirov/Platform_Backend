import os
import boto3
from botocore.client import Config

session = boto3.session.Session()
client = session.client('s3',
                        region_name='fra1',
                        endpoint_url='https://fra1.digitaloceanspaces.com',
                        aws_access_key_id='DO00BWNCXJDR3ZJF9KVJ',
                        aws_secret_access_key='dop_v1_3be20c6054521e0df86de47776093d0946339945de7bcbe3eae3e32f52544f0d')


AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = 'noxonfx'
AWS_ENDPOINT_URL = "https://fra1.digitaloceanspaces.com"
AWS_ENDPOINT = "fra1.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
DEFAULT_FILE_STORAGE = "core.cdn.backends.MediaRootS3Boto3Storages"
STATICFILES_STORAGE = "core.cdn.backends.StaticRootS3Boto3Storages"