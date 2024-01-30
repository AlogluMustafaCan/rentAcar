FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY app ./app

EXPOSE 8080

ENTRYPOINT [ "python3", "-m", "app" ]