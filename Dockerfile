FROM python:3.12
FROM mcr.microsoft.com/playwright/python:v1.50.0-noble

ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt -v

COPY src /src

EXPOSE 8000

CMD ["streamlit", "run", "main.py"]
