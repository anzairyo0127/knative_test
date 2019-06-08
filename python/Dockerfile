FROM python:3.7.3-alpine
RUN pip install -U pip
COPY ./ /var/app/
WORKDIR /var/app
RUN pip install -r ./requirements.txt
ENV FLASK_ENV development
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app

