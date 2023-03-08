import csv
import requests
import boto3
import argparse
import os
from pathlib import Path

def main():
    # let's get the path to the file
    csv_path = Path(get_args())
    print(csv_path)

    # get the csv, which should just be 1 column w/ the uuid's to grab, and should include a header column as noted on row 17
    with open(csv_path) as csv_file:
        return process_images(csv_file)

def process_images(csv_file):
    s3 = boto3.resource('s3') 
    s3_bucket_name = "pnca-web-components"
    base_url = "https://calendarmedia.blob.core.windows.net/assets/"
    base_extension = ".jpg"
    base_extension_small = "-small.jpg"
    s3_path = "colindev/originals/"
    s3_path_small = "colindev/smalls/"
    data_folder = Path("./")
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    # do each
    for row in csv_reader:

        # ignore row one,as for some reason if you don't have a header it freaks out on the first row and makes an immutable local object....good times
        if line_count == 0:
            print(f'HEADER{(row)}')
            print(row[0])
            line_count += 1

        # now we get to the meat of the script
        else:
            print(row[0])
            # grab the uuid from the csv
            image_uuid = row[0]

            # set the filename
            image_name = image_uuid + base_extension
            # set the url string for the original
            image_url = base_url + image_uuid + base_extension
            # and where to save it locally
            image_path = data_folder / image_name

            # grab the actual image content
            img_data = requests.get(image_url).content
            # and write it to our defined file
            with open(image_path, 'wb') as h1:
                h1.write(img_data)

            # now let's move the original to s3
            with open(image_path, "rb") as f1:
                s3.Bucket(s3_bucket_name).put_object(Key=s3_path + image_name, Body=f1)

            # last we'll purge the local file
            os.remove(image_path)

            # NOW WE DO THE SAME WITH THE SMALLS

            # set the filename
            image_name_small = image_uuid + base_extension_small
            # set the url string for the small
            image_url_small = base_url + image_name_small
            # and where to save it locally
            image_path_small = data_folder / image_name_small

            # grab the actual image content
            img_data_small = requests.get(image_url_small).content
            # and write it to our defined file
            with open(image_path_small, 'wb') as h2:
                h2.write(img_data_small)

            # now let's move the small to s3
            with open(image_path_small, "rb") as f2:
                s3.Bucket(s3_bucket_name).put_object(Key=s3_path_small + image_name_small, Body=f2)

            # last we'll purge the local file
            os.remove(image_path_small)

            # iterate the count
            line_count += 1
    print(f'Processed {line_count} lines.')

def get_args():

        path =''

        parser = argparse.ArgumentParser(
        description='Path to run check file')
        parser.add_argument('-p', '--path', type=str,help='path of the file that you want to check for outliers ,stale and missing data ',required = True)
        args = parser.parse_args()

        ''' Assign args to variables'''

        path = args.path
        return path
