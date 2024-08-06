FROM python:3.12.2

COPY backend /opt/backend
COPY telegram_bot /opt/telegram_bot
COPY database_api /opt/database_api
COPY main.py /opt
WORKDIR /opt

RUN apt update && apt install -y python3-dev default-libmysqlclient-dev build-essential pkg-config

RUN pip install --upgrade pip && pip install -r /opt/backend/requirements.txt
ENTRYPOINT ["python", "main.py"]