FROM python:alpine
COPY ./requirements.txt /home/flask/requirements.txt
WORKDIR /home/flask
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /home/flask
CMD ["python", "/home/flask/main.py" ]