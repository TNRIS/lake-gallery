
FROM ubuntu:xenial

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-venv python3-dev nginx supervisor curl

# Setup python 3 virtualenv
RUN mkdir /envs/
RUN python3 -m venv /envs/lake-gallery
ENV PATH /envs/lake-gallery/bin:$PATH
# upgrade pip
RUN pip3 install -U pip


# install awscli
RUN pip3 install awscli

# set aws region
ENV AWS_REGION us-east-1

COPY /docker-entrypoint.sh /
COPY /docker-entrypoint.d/* /docker-entrypoint.d/
ONBUILD COPY /docker-entrypoint.d/* /docker-entrypoint.d/

RUN chmod +x docker-entrypoint.sh
RUN chmod +x docker-entrypoint.d/*.sh

# Setup app
COPY lakegallery /lakegallery/
RUN pip3 install -r /lakegallery/requirements.txt --upgrade
RUN pip3 install gunicorn

# Setup Django environment
ENV PYTHONPATH $PYTHONPATH: /lakegallery
ENV DJANGO_SETTINGS_MODULE lakegallery.settings

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
COPY django.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/django.conf /etc/nginx/sites-enabled/django.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Setup supervisord
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

# Expose port
EXPOSE 1970

# Run entrypoint script
ENTRYPOINT ["/docker-entrypoint.sh"]