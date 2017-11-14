.PHONY: run-dev run-prod

run-dev:
	export LAKE_GALLERY_MODE='DEVELOPMENT' && \
	. ./lakegallery/secrets/set_env.sh && \
	python manage.py runserver

run-prod:
	export LAKE_GALLERY_MODE='PRODUCTION' && \
	. ./lakegallery/secrets/set_env.sh && \
	python manage.py runserver

push-static:
	export LAKE_GALLERY_MODE='PRODUCTION' && \
	. ./lakegallery/secrets/set_env.sh && \
	python manage.py collectstatic

run-tests:
	export LAKE_GALLERY_MODE='DEVELOPMENT' && \
	. ./lakegallery/secrets/set_env.sh && \
	python manage.py test map.tests
