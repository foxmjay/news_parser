FROM python:2.7
add . /code
WORKDIR /code
run pip install -r requirements.txt
CMD python server.py
