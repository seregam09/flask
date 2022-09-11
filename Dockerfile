FROM python:3.8
COPY ./requirements.txt /home/flask/requirements.txt
WORKDIR /home/flask
RUN pip install -r requirements.txt
COPY . /home/flask
CMD ["python", "/home/flask/main.py" ]