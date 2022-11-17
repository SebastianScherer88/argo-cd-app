FROM python:3.10

WORKDIR /repository

ENV PYTHONPATH /repository

COPY ./requirements.txt /repository/requirements.txt
COPY ./app /repository/app
COPY ./tests /repository/tests

RUN pip install --no-cache-dir --upgrade -r /repository/requirements.txt

ENV API_PORT = 8000

CMD ["python", "app/api:app"]