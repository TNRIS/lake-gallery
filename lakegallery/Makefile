
run-dev:
	LAKE_GALLERY_MODE='DEVELOPMENT' \
	python manage.py runserver

run-prod:
	LAKE_GALLERY_MODE='PRODUCTION' \
	python manage.py runserver

push-static:
	LAKE_GALLERY_MODE='PRODUCTION' \
	python manage.py collectstatic

run-tests:
	LAKE_GALLERY_MODE='DEVELOPMENT' \
	python manage.py test map
