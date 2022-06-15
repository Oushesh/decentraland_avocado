'''
aws cdk_cli
Boto3
upload_file
'''

import boto3
s3_client = boto3.client('s3')

def upload_file_s3(file_path,bucket_name,target_path):
    response = s3_client.upload_file(file_path,bucket_name,target_path)
    try:
        s3_client.upload_file(file_path,bucket_name,target_path)
    except ClientError as error:
        raise S3UlpoadFailedError("Failed to upload %s" % (file_path, e))
    return None

'''
Input: Folder
aws s3 bucket
Target_folder
'''

def upload_folder(folder_path,bucket_name,target_folder):
    upload_folder(folder_path,bucket_name,)
    return None

if __name__ == "__main__":
    file_path  = r'C:\Users\oushe\Documents\WORKSPACE\versadex\$WORKON_HOME\decentraland_avocado\models\Avocado.bin'
    bucket_name = 'glbbucket007'
    target_path = 'avocado.bin'

    folder_path = model_path

    upload_file_s3(file_path,bucket_name,target_path)
    upload_folder_s3()
