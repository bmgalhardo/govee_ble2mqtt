import os

from bluepy.btle import Scanner
import paho.mqtt.client as mqtt

from utils import ScanDelegate

if __name__ == "__main__":
    client = mqtt.Client()
    mqtt_prefix = os.getenv("MQTT_PREFIX", "homeassistant/sensor")
    mqtt_uri = os.getenv("MQTT_URI", "localhost")
    mqtt_port = int(os.getenv("MQTT_PORT", 1883))

    scanner = Scanner().withDelegate(ScanDelegate(client, mqtt_prefix))
    client.connect(mqtt_uri, mqtt_port, 60)

    while True:
        scanner.scan(60.0, passive=True)

