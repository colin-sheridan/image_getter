Requirements:
boto3
path
requests
pytest
argparse
poetry-dotenv-plugin

Setup:
    - Install AWS CLI and run 'aws setup' to set access key / secret
    - Create a .env file in the root of this project w/ the following:
        S3_BUCKET="" - The name of the target s3 bucket
        BASE_URL="" - The base asset url
        S3_PATH_ORIGINAL="" - The path in the S3 bucket for the originals
        S3_PATH_SMALL="" - The path in the S3 bucket for the small ones
    - Run 'poetry install'

Usage (from ./image_getter):
poetry run process -p '***ABSOLUTE PATH TO CSV***'
