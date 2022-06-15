echo "Installation Instructions of Decentraland"

echo 'Downloading Unzipping the smart item'

python executor.py
#python aws_cdk_uploader.py
echo 'uploding the glb models'
aws s3 sync models s3://glbbucket007/models
