.PHONY: run-dev run-prod

run-dev:
	LAKE_GALLERY_MODE='DEVELOPMENT' && \
	. ./lakegallery/secrets/set_env.sh && \
	python manage.py runserver

run-prod:
	LAKE_GALLERY_MODE='PRODUCTION' && \
	. ./lakegallery/secrets/set_env.sh && \
	python manage.py runserver

push-static:
	export LAKE_GALLERY_MODE='PRODUCTION' && \
	. ./lakegallery/secrets/set_env.sh && \
	python manage.py collectstatic

run-tests:
	LAKE_GALLERY_MODE='DEVELOPMENT' \
	python manage.py test map
