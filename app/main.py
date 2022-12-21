import argparse

from bluepy.btle import Scanner
import paho.mqtt.client as mqtt

from utils import ScanDelegate

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process raw data acquisition measurements')
    parser.add_argument('--host', help='mqtt uri', default="localhost")
    parser.add_argument('--port', help='mqtt port', default="1883")
    parser.add_argument('--topic', help='mqtt topic', default="homeassistant/sensor")
    args = parser.parse_args()

    client = mqtt.Client()
    scanner = Scanner().withDelegate(ScanDelegate(client, args.topic))
    client.connect(args.host, int(args.port), 60)

    while True:
        scanner.scan(60.0, passive=True)

