##here we git clone from our git

echo 'updating the models here locally from the website:'
aws s3 sync s3://glbbucket007/models downloaded_models
