FROM python:3.10-slim-buster
ADD . /QAProject-ExpenseTracker
WORKDIR /QAProject-ExpenseTracker
COPY .  .
RUN pip install flask

CMD [ "python", "app.py" ]
