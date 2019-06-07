FROM python:3.7.3-alpine
COPY ./ /var/app/
WORKDIR /var/app
RUN pip install -r ./requirements.txt
CMD ["python", "app.py"]
