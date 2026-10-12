FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt -v && playwright install --with-deps chromium

COPY src /src

EXPOSE 8000

CMD ["streamlit", "run", "main.py"]
