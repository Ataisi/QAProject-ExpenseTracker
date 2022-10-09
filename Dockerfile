FROM python:3.10-slim-buster
ADD . /QAProject-ExpenseTracker
WORKDIR /QAProject-ExpenseTracker
RUN apt-get update && apt-get install -y python3-pip
COPY requirements.txt 
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python", " /app.py" ]
