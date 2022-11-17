FROM python:3.10

WORKDIR /repository

COPY ./requirements.txt /repository/requirements.txt
COPY ./app /repository/app
COPY ./tests /repository/tests

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV API_PORT = 8080

CMD ["python", "app/api:app"]