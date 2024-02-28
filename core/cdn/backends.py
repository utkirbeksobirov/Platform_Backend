from storages.backends.s3boto3 import S3Boto3Storage
import boto3

client = boto3.client('amplifybackend')

class StaticRootS3Boto3Storages(S3Boto3Storage):
    location = 'static'

class MediaRootS3Boto3Storages(S3Boto3Storage):
    location = 'media'
