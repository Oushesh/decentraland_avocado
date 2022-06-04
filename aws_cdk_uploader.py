'''
aws cdk_cli
Boto3
upload_file
'''

import boto3

s3_client = boto3.client('s3')

#perform file check that the 2 file have the same endings

def upload_file_s3(file_path,bucket_name,target_path):
    response = s3_client.upload_file(file_path,bucket_name,target_path)
    try:
        s3_client.upload_file(file_path,bucket_name,target_path)
    except ClientError as error:
        raise S3UlpoadFailedError("Failed to upload %s" % (file_path, e))
    return None

#https://bobbyhadz.com/blog/aws-s3-copy-local-folder-to-bucket#:~:text=To%20copy%20a%20local%20folder,Copied!

'''
Input: Folder
aws s3 bucket
Target_folder
'''

def upload_folder(folder_path,bucket_name,target_folder):
    folder_name = folder_path.split("\\")[-1]
    assert (os.path.isdir(folder_name)==True)
    for subdir,dirs,files in os.walk(folder_path):
        for file in files:
    return None

#>aws s3 sync models s3://glbbucket007/models



if __name__ == "__main__":
    file_path  = r'C:\Users\oushe\Documents\WORKSPACE\versadex\$WORKON_HOME\decentraland_avocado\models\Avocado.bin'
    bucket_name = 'glbbucket007'
    target_path = 'avocado.bin'

    folder_path =

    upload_file_s3(file_path,bucket_name,target_path)
    upload_folder_s3()

##Added sync functions as well to bucket
##I can also sync both ways local to s3, s3 to lacal bucket
