FROM python:alpine3.21

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./code/ /code/

CMD ["fastapi", "run", "main.py", "--port", "80"]
