FROM python:3

ENV PYTHONUNBEFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r ./requirements.txt

COPY run.py /app/run.py

COPY scrapy.cfg /app/scrapy.cfg

COPY crawler app/crawler

CMD python run.py
