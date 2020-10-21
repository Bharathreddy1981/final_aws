from flask import Flask,jsonify
import logging
import boto3
from botocore.exceptions import ClientError
from botocore.client import Config

aws_get_totoal_url_1111 = Flask(__name__)


@aws_get_totoal_url_1111.route("/get", methods=["GET"])

def create_presigned_url():
    ACCESS_KEY_ID = "AKIAZNN5NBT72GR3NKP7"
    ACCESS_SECRET_KEY = "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"
    AWS_DEFAULT_REGION = 'ap-south-1'
    s3_client = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        region_name=AWS_DEFAULT_REGION,
        config=Config(signature_version='s3v4')
    )
    my_bucket = s3_client.Bucket('flask121')

    list= []
    for file in my_bucket.objects.all():
        value = file.key
        # print(a)

        def create_presigned_url(bucket_name, object_name, expiration=3600,signature_version='s3v4'):
            s3_client = boto3.client(
                "s3",
                aws_access_key_id=ACCESS_KEY_ID,
                aws_secret_access_key=ACCESS_SECRET_KEY,
                region_name=AWS_DEFAULT_REGION,
                config=Config(signature_version="s3v4")
                )
            try:
                response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=3600)
            except ClientError as e:
                    logging.error(e)
                    return None

            return response

        url=create_presigned_url("flask121", value, expiration=3600,signature_version='s3v4')

        list.append({value: url})

    return jsonify(list)

if __name__=="__main__":
    aws_get_totoal_url_1111.run(host='0.0.0.0')