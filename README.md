# Govee BLE to MQTT

Adapted original code for running in docker environments.

Note: ensure bluez is not running on the host

## Configuration
Define the arguments according to your broker settings:
- --topic, default=homeassistant/sensor
- --host, default=localhost
- --port, default=1883

## Running locally

```commandline
docker-compose build
docker-compose up -d
```