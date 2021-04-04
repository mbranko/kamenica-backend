FROM python:3.9-slim-buster
MAINTAINER Branko Milosavljevic <mbranko@uns.ac.rs>
RUN apt -y update
RUN apt -y install gcc libmariadb-dev-compat graphviz-dev libffi-dev libmagic1 libtiff-dev libopenjp2-7-dev liblcms-dev zlib1g-dev libjpeg-dev musl-dev uwsgi uwsgi-plugin-python3 uwsgi-plugin-router-access
RUN pip3 install -U pip setuptools
COPY app/requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
COPY app /app
RUN mkdir -p /app/static
WORKDIR /app
RUN mkdir /private
RUN echo "SECRET_KEY=XYZ" > /private/secrets
RUN rm -rf /app/log
RUN mkdir /app/log
ARG django_settings=prod
ENV DJANGO_SETTINGS=$django_settings
RUN python3 /app/manage.py collectstatic --noinput
RUN rm -rf /app/log/*
RUN rm -rf /private
RUN chmod +x /app/run_prod.sh
EXPOSE 8000
ENTRYPOINT ["/app/run_prod.sh"]
