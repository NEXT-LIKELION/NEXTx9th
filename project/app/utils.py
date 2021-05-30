from .models import Post
from crudproject.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
import boto3
from boto3.session import Session
from datetime import datetime

# s3 = boto3.client('s3')

# bucket_name = 'hackathon-zzalpangi'

# file_name = "file-name.png"

# s3.


def upload_and_save(request, file_to_upload):
    # client 만들기
    session = Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_S3_REGION_NAME
    )
    s3 = session.resource('s3')

    # s3에 object 업로드
    now = datetime.now().strftime("%U%H%M%S")
    img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
        Key=now + file_to_upload.name,
        Body=file_to_upload
    )

    # Post model 만들기
    s3_url = 'https://hackathon-zzalpangi.s3.ap-northeast-2.amazonaws.com/'
    post = Post.objects.create(
        img=s3_url + now + file_to_upload.name
    )
