# lake-gallery
Web Map for exploring the history of Texas lakes

## Setup
Built with:
* Python 3.5 (virtual environment suggested)
* PostgreSQL 9.5.2
  * Amazon RDS Instance
* [Django](https://docs.djangoproject.com/en/1.11/topics/install/)


1. Enable your virtual environment. Example- `workon django`
2. Upgrade pip using `pip install --upgrade pip`
3. `cd ./lakegallery` and install python requirements `pip install -r requirements.txt`
4. cd into the secrets folder of the repo `cd ./lakegallery/lakegallery/secrets/`
5. place a copy `vault-password.txt` into the secrets folder of the repo (You might need to change spaces to newlines) and run `make pull-secrets`
  
  or

5. make a copy of the secrets-sample.py, remove the '-sample' from the name, and manually fill in the values

It is suggested to use your locally configured AWS CLI when working locally. If this is already set up, you can ignore the AWS Key & Secret in the secrets.py file. If not, you will need to populate them in secrets.py and uncomment these parameters within the app's settings.py

## Develop
1. `cd ./lakegallery` and run `make run-dev` to run the app locally and reference local static files. Will be available at `localhost:8000`. Media files will still be referenced from the production S3 bucket.

## Production Build
In production, the app pulls/references all static files for all apps from the configured S3 bucket. Run **Deploy** Step 1 to upload push local static files into S3. **VERY DANGEROUS** if app is currently deployed as you will be overwriting the production static files!
1. `cd ./lakegallery` and run `make run-prod` to run the app locally and reference prod s3 static files. Will be available at `localhost:8000`.

## Deploy
1. `cd ./lakegallery` and run `make push-static` to compile all static files and overwrite those in S3. **VERY DANGEROUS** if app is currently deployed as you will be overwriting the production static files!


## Notes
* [Django Tutorial](https://docs.djangoproject.com/en/1.11/intro/)
