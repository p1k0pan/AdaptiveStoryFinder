FROM python:3.8.16
WORKDIR /code
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y vim
RUN pip install -r requirements.txt
# CMD ["python", "manage.py", "runserver"]
