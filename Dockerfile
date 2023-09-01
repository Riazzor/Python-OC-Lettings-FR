FROM python:3.11.5-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
ENTRYPOINT ["python"]

EXPOSE 8000

CMD ["manage.py", "runserver", "0.0.0.0:8000"]
