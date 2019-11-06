FROM python:3-alpine

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:5000", "app:app"]

USER 1000:0

