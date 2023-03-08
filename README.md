
# Image Getter

Useful to grab images from a remote source and place them into AWS s3 paths





## Installation
Install Poetry (see https://python-poetry.org/docs/)

Install AWS CLI and run 'aws setup' to set access key / secret

Run 'poetry install'
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`S3_BUCKET`
The name of the target s3 bucket

`BASE_URL`
The base asset url

`S3_PATH_ORIGINAL`
The path in the S3 bucket for the originals

`S3_PATH_SMALL`
The path in the S3 bucket for the small ones
## Usage/Examples

from the "./image_getter" directory:
```
poetry run process -p '***ABSOLTE PATH TO CSV***'
```

