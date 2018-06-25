FROM python:3.6

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD *.py ./

EXPOSE 5000

CMD python server.py --host=$HOST --port=$PORT --db=$DB