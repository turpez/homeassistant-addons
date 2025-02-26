FROM python:3.10

WORKDIR /app

COPY addon.py /app/
COPY config.json /app/

RUN pip install requests

CMD ["python", "/app/addon.py"]
