#!/bin/bash

export SECRET_KEY=`/envs/lake-gallery/bin/aws ssm get-parameters --name /apps/lake_gallery/secret_key --with-decryption --region us-east-1 --output text | awk '{print $6}'`

export DB_NAME=`/envs/lake-gallery/bin/aws ssm get-parameters --name /apps/lake_gallery/db_name --with-decryption --region us-east-1 --output text | awk '{print $6}'`
export DB_USER=`/envs/lake-gallery/bin/aws ssm get-parameters --name /apps/lake_gallery/db_user --with-decryption --region us-east-1 --output text | awk '{print $6}'`
export DB_PASSWORD=`/envs/lake-gallery/bin/aws ssm get-parameters --name /apps/lake_gallery/db_password --with-decryption --region us-east-1 --output text | awk '{print $6}'`
export DB_HOST=`/envs/lake-gallery/bin/aws ssm get-parameters --name /apps/lake_gallery/db_host --with-decryption --region us-east-1 --output text | awk '{print $6}'`
export DB_PORT=`/envs/lake-gallery/bin/aws ssm get-parameters --name /apps/lake_gallery/db_port --with-decryption --region us-east-1 --output text | awk '{print $6}'`

export AWS_STORAGE_BUCKET_NAME=`/envs/lake-gallery/bin/aws ssm get-parameters --name /apps/lake_gallery/aws_storage_bucket_name --region us-east-1 --output text | awk '{print $6}'`
export AWS_S3_REGION_NAME=`/envs/lake-gallery/bin/aws ssm get-parameters --name /apps/lake_gallery/aws_s3_region_name --with-decryption --region us-east-1 --output text | awk '{print $6}'`

export CONTACT_SUBMIT_URL=`/envs/lake-gallery/bin/aws ssm get-parameters --name /apps/lake_gallery/contact_submit_url --region us-east-1 --output text | awk '{print $6}'`
export RECAPTCHA_SITE_KEY=`/envs/lake-gallery/bin/aws ssm get-parameters --name /apps/lake_gallery/recaptcha_site_key --region us-east-1 --output text | awk '{print $6}'`

export LAKE_GALLERY_MODE=`/envs/lake-gallery/bin/aws ssm get-parameters --name /apps/lake_gallery/lake_gallery_mode --region us-east-1 --output text | awk '{print $6}'`

eval /lakegallery/manage.py collectstatic --noinput "$@"
eval /usr/bin/supervisord "$@"
