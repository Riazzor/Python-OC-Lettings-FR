FROM python:3.11.5-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y git
RUN apt-get install -y openssh-server
RUN apt-get install -y tar
RUN apt-get install -y gzip
RUN apt-get install -y ca-certificates

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
