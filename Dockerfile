FROM python:3.6

WORKDIR /app

COPY app/requirements /app/requirements
RUN pip install --trusted-host pypi.python.org -r requirements/base.txt

COPY .env /
COPY ./app /app

EXPOSE 8000
