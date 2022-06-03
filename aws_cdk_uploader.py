'''
aws cdk_cli
Boto3
upload_file
'''

import boto3

s3_client = boto3.client('s3')

#perform file check that the 2 file have the same endings
response = s3_client.upload_file(r'C:\Users\oushe\Documents\WORKSPACE\versadex\$WORKON_HOME\decentraland_avocado\models\Avocado.gltf','glbbucket007','avocado.gltf')
