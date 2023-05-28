FROM python:3.10

RUN mkdir -p /usr/src/web/

WORKDIR /usr/src/web/

COPY . /usr/src/web/

RUN pip install -r requirements.txt
RUN pip install psycopg2

RUN make build

EXPOSE 8000
