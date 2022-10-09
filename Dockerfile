FROM python:3.10-slim-buster
ADD . /students
WORKDIR /students
COPY . .
RUN pip install flask
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "app.py" ]
