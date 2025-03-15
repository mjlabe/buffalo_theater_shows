FROM python:3.12
FROM mcr.microsoft.com/playwright/python:v1.50.0-noble

WORKDIR /code

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt -v

COPY ./src /src

EXPOSE 8000

CMD ["streamlit", "run", "app.py"]
