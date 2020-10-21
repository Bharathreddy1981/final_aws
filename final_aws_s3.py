from flask import Flask,jsonify,request
import boto3
from botocore.client import Config

final_aws = Flask(__name__)

@final_aws.route("/aws", methods=["POST"])
def bun():
    data = request.get_json()
    ACCESS_KEY_ID = "AKIAZNN5NBT72GR3NKP7"
    ACCESS_SECRET_KEY = "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"
    BUCKET_NAME = "flask121"

    data = open(data["image"], 'rb')

    s3 = boto3.resource(
        "s3",
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version="s3v4")
    )
    s3.Bucket(BUCKET_NAME).put_object(Key="nat.jpg", Body=data)

    print("Done")

    base_url = 'https://flask121.s3.ap-south-1.amazonaws.com/'
    file_name = 'nat.jpg'
    final_url = base_url + file_name

    return jsonify({'url': final_url})


if __name__=="__main__":
    final_aws.run(host='0.0.0.0')
