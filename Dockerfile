FROM python:3.10-slim-buster
ADD . /QAProject-ExpenseTracker
WORKDIR /QAProject-ExpenseTracker
COPY . .
RUN pip install flask
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "app.py" ]
