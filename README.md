# lake-gallery
Web Map for exploring the history of Texas lakes

## Setup
Built with:
* Python 3.5 (virtual environment suggested)
* PostgreSQL 9.5.2
  * Amazon RDS Instance

Install:
* Upgrade pip using `pip install --upgrade pip`
* [psycopg2](http://initd.org/psycopg/) using `pip install psycopg2`
* [Django](https://docs.djangoproject.com/en/1.11/topics/install/) using `pip install Django`

1. cd into the secrets folder of the repo `cd ./lakegallery/lakegallery/secrets/`
2. place a copy `vault-password.txt` into the secrets folder of the repo (You might need to change spaces to newlines) and run `make pull-secrets`
  or
2. make a copy of the secrets-sample.py, remove the '-sample' from the name, and manually fill in the values


## Notes
* [Django Tutorial](https://docs.djangoproject.com/en/1.11/intro/)