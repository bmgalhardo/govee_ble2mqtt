FROM python:3.4-slim

RUN apt-get update -y && \
    apt-get install -y make libglib2.0-dev build-essential git bluez \
    /etc/init.d/dbus start

RUN git clone https://github.com/IanHarvey/bluepy.git
WORKDIR bluepy
RUN python setup.py build
RUN python setup.py install

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

COPY app/ /app
WORKDIR /app

CMD ["python", "main.py"]

