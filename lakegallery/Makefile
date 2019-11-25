.PHONY: run-dev run-dev-local run-prod

run-dev:
	export LAKE_GALLERY_MODE='DEVELOPMENT' && \
	. ./lakegallery/secrets/set_env.sh && \
	python manage.py collectstatic && \
	python manage.py runserver

run-dev-local:
	export LAKE_GALLERY_MODE='DEVELOPMENT' && \
	. ./lakegallery/secrets/set_env.sh && \
	python manage.py collectstatic && \
	python manage.py runserver 0.0.0.0:8030

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
