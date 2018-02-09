# Texas Lake Gallery
Web Map for exploring the history of Texas lakes

`cd ./lakegallery` as all commands are run from the ~/lake-gallery/lakegallery/ directory

## Setup
Built with:
* Python 3.5 ([virtual environment](https://howchoo.com/g/nwewzjmzmjc/a-guide-to-python-virtual-environments-with-virtualenvwrapper) suggested)
* PostgreSQL 9.5.2
  * Amazon RDS Instance
* [GDAL](http://www.gdal.org/) & GDAL Python & GDAL Devel
* [Django](https://docs.djangoproject.com/en/2.0/topics/install/)
* For data scripts, you probably want to use some form of python virtual env manager to maintain an isolated environment. A good run-down of the options can be found in [The Hitchiker's Guide to Python](http://docs.python-guide.org/en/latest/dev/virtualenvs/). A recommended setup is virtualenv + virtualenvwrapper. [Anaconda](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/) is an alternative but it has not been successfully tested.


1. Enable your virtual environment. Example- `workon lakegallery` (for virtualenv wrapper)
2. Upgrade pip using `pip install --upgrade pip`
3. install python requirements `pip install -r requirements.txt`
4. cd into the secrets folder of the repo `cd ./lakegallery/lakegallery/secrets/`
5. place a copy `vault-password.txt` into the secrets folder of the repo (You might need to change spaces to newlines) and run `make pull-secrets`

  or

5. make a copy of the set_env-SAMPLE.sh, remove the '-SAMPLE' from the name, and manually fill in the values. Then run `. set_env.sh` from said secrets folder

You will need to use your configured AWS CLI when working locally. If not already set up, you will need to install the AWS CLI and configure it with an access key and secret key.

## Develop

1. Make sure `DEBUG = True` in ~/lake-gallery/lakegallery/lakegallery/settings.py
1. run `make run-dev` to run the app locally and reference local static files. Will be available at `localhost:8000`. Media files will still be referenced from the production S3 bucket.
1. run `make run-tests` to run the unit tests for the map application

## Local Production Build

In production, the app pulls/references all static files for all apps from the configured S3 bucket. Run **Deployment Prep** section's Step 1 to upload/push local static files into S3. **VERY DANGEROUS** if app is currently deployed as you will be overwriting the production static files!
1. Make sure `DEBUG = True` in ~/lake-gallery/lakegallery/lakegallery/settings.py
1. run `make run-prod` to run the app locally and reference prod s3 static files. Will be available at `localhost:8000`.

## Deployment Prep

1. Make sure `DEBUG = False` in ~/lake-gallery/lakegallery/lakegallery/settings.py
1. run `make push-static` to compile all static files and overwrite those in S3. **VERY DANGEROUS** if app is currently deployed as you will be overwriting the production static files!
1. `pip freeze > requirements.txt` to save dependencies
1. head over to the deployments repo to execute the actual application deployment


## Notes
* [Django Tutorial](https://docs.djangoproject.com/en/1.11/intro/)
