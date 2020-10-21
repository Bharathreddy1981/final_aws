from flask import Flask,jsonify
import boto3
from botocore.client import Config
import botocore


aws_get_totoal_url = Flask(__name__)


@aws_get_totoal_url.route("/total", methods=["GET"])
def cat():
    ACCESS_KEY_ID = "AKIAZNN5NBT72GR3NKP7"
    ACCESS_SECRET_KEY = "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"
    AWS_DEFAULT_REGION = 'ap-south-1'



    s3=boto3.resource(
        "s3",
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        region_name=AWS_DEFAULT_REGION,
        config=Config(signature_version="s3v4")
    )
    bucket = "flask121"
    my_bucket=s3.Bucket(bucket)

    list=[]
    for files in my_bucket.objects.all():

        value=files.key
        #print(files.key)

        #list.append(key)

        my_config = Config(
            signature_version=botocore.UNSIGNED)  # instead of botocore.UNSIGNED use 's3v4' for better url
        s3_client = boto3.client('s3', config=my_config)

        params = {"Bucket": 'flask121', "Key": value}
        url = s3_client.generate_presigned_url('get_object', params, ExpiresIn=3600)
        # print({value: url})

        list.append({value: url})




    return jsonify(list)


if __name__=="__main__":
    aws_get_totoal_url.run(host='0.0.0.0')