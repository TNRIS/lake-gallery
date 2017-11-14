#!/bin/bash

export SECRET_KEY=''

export DB_NAME=''
export DB_USER=''
export DB_PASSWORD=''
export DB_HOST=''
export DB_PORT=''

export AWS_STORAGE_BUCKET_NAME=''
export AWS_S3_REGION_NAME=''

echo 'Environment variables set!'

# PSQL CONNECT:
# psql -d db_name -h db_host -p db_port -U db_user