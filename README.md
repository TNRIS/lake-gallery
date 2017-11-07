# lake-gallery
Web Map for exploring the history of Texas lakes

`cd ./lakegallery` as all commands are run from the ~/lake-gallery/lakegallery/ directory

## Setup
Built with:
* Python 3.5 (virtual environment suggested)
* PostgreSQL 9.5.2
  * Amazon RDS Instance
* [Django](https://docs.djangoproject.com/en/1.11/topics/install/)


1. Enable your virtual environment. Example- `workon django`
2. Upgrade pip using `pip install --upgrade pip`
3. install python requirements `pip install -r requirements.txt`
4. cd into the secrets folder of the repo `cd ./lakegallery/lakegallery/secrets/`
5. place a copy `vault-password.txt` into the secrets folder of the repo (You might need to change spaces to newlines) and run `make pull-secrets`
  
  or

5. make a copy of the set_env-SAMPLE.sh, remove the '-SAMPLE' from the name, and manually fill in the values. Then run `. set_env.sh` from said secrets folder

You will need to use your configured AWS CLI when working locally. If not already set up, you will need to install the AWS CLI and configure it with an access key and secret key.

## Develop
1. run `make run-dev` to run the app locally and reference local static files. Will be available at `localhost:8000`. Media files will still be referenced from the production S3 bucket.
1. run `make run-tests` to run the unit tests for the map application

## Production Build
In production, the app pulls/references all static files for all apps from the configured S3 bucket. Run **Deploy** Step 1 to upload push local static files into S3. **VERY DANGEROUS** if app is currently deployed as you will be overwriting the production static files!
1. run `make run-prod` to run the app locally and reference prod s3 static files. Will be available at `localhost:8000`.

## Deploy
1. run `make push-static` to compile all static files and overwrite those in S3. **VERY DANGEROUS** if app is currently deployed as you will be overwriting the production static files!


## Notes
* [Django Tutorial](https://docs.djangoproject.com/en/1.11/intro/)
