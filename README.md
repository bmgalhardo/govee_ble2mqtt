# Govee BLE to MQTT

Adapted original code for running in docker environments.
## Configuration
Define the environmental variables according to your needs:
- MQTT_PREFIX, default=homeassistant/sensor
- MQTT_URI, default=localhost
- MQTT_PORT, default=1883
## Running

```commandline
docker-compose build
docker-compose up -d
```