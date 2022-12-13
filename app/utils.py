from bluepy.btle import DefaultDelegate


class ScanDelegate(DefaultDelegate):

    def __init__(self, client, mqtt_prefix):
        super().__init__()
        self.client = client
        self.mqtt_prefix = mqtt_prefix

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if dev.addr[:8] == "a4:c1:38":

            # returns a list, of which the [2] item of the [3] tuple is manufacturing data
            adv_list = dev.getScanData()
            adv_manuf_data = adv_list[2][2]
            print(adv_manuf_data)
            # this is the location of the encoded temp/humidity and battery data
            temp_hum_data = adv_manuf_data[6:12]
            battery = adv_manuf_data[12:14]

            try:
                val = int(temp_hum_data, 16)
                # decode tip from eharris: https://github.com/Thrilleratplay/GoveeWatcher/issues/2
                is_negative = False
                if val & 0x800000:
                    is_negative = True
                    val = val ^ 0x800000
                temp = int(val / 1000) / 10
                if is_negative:
                    temp = 0 - temp
            except ValueError:
                temp = None

            try:
                battery_percent = int(battery) / 64 * 100
                battery_percent = round(battery_percent)
            except ValueError:
                battery_percent = None

            try:
                hum_percent = ((int(temp_hum_data, 16)) % 1000) / 10
                hum_percent = round(hum_percent)
            except ValueError:
                hum_percent = None

            mqtt_topic = self.mqtt_prefix + "/" + dev.addr

            self.client.publish(mqtt_topic + "/rssi", dev.rssi, qos=0)
            self.client.publish(mqtt_topic + "/temp_C", temp, qos=0)
            self.client.publish(mqtt_topic + "/hum_perc", hum_percent, qos=0)
            self.client.publish(mqtt_topic + "/battery_perc", battery_percent, qos=0)
