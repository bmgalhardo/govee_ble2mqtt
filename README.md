# Govee BLE to MQTT

Adapted original code for running in docker environments.

Note: ensure bluez is not running on the host

## Configuration
Define the environmental variables according to your needs:
- MQTT_PREFIX, default=homeassistant/sensor
- MQTT_URI, default=localhost
- MQTT_PORT, default=1883

## Running locally

```commandline
docker-compose build
docker-compose up -d
```