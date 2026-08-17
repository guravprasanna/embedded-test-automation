device_1 = {"device_id":"BT001","device_type": "Universal Node", "hardware": ("ESP32","v2.1","Rev-B"), "sensors": {"temperature": 32.5, "humidity": 48.0, "voltage": 12.00, "current": 0.45}}
device_2 = {"device_id":"BT002","device_type": "HVAC Node", "hardware": ("ESP32","v2.1","Rev-B"), "sensors": { "temperature": 42.5, "humidity": 38.0, "voltage": 4.00, "current": 0.80}}
device_3 = {"device_id":"BT003","device_type": "Eight Point Node", "hardware": ("ESP32","v2.1","Rev-B"), "sensors": { "temperature": 18.5, "humidity": 58.0, "voltage": 12.00, "current": 1.50}}
devices = [device_1, device_2, device_3]
unique_device_ids = set()
unique_device_types = set()
highest_temperature = None
highest_temperature_device = None
lowest_voltage = None
lowest_voltage_device = None

for device in devices:
    print(f"Device ID: {device['device_id']}")
    print(f"Device Type: {device['device_type']}")
    print(f"MCU: {device["hardware"][0]}")
    print(f"Version: {device["hardware"][1]}")
    print(f"Revision: {device["hardware"][2]}")
    print(f"Temperature: {device["sensors"]["temperature"]}")
    print(f"Humidity: {device["sensors"]["humidity"]}")
    print(f"Voltage: {device["sensors"]["voltage"]}")
    print(f"Current: {device["sensors"]["current"]}")
    print("---------------------")
    unique_device_ids.add(device["device_id"])
    unique_device_types.add(device["device_type"])
for device in devices:
    temperature = device["sensors"]["temperature"]
    if highest_temperature is None or temperature >= highest_temperature:
        highest_temperature = temperature
        highest_temperature_device = device["device_id"]
for device in devices:
    voltage = device["sensors"]["voltage"]
    if lowest_voltage is None or voltage <= lowest_voltage:
        lowest_voltage = voltage
        lowest_voltage_device = device["device_id"]
print(f"Highest Temperature: {highest_temperature} °C")
print(f"Device with Highest Temperature: {highest_temperature_device}")
print(f"Lowest Voltage: {lowest_voltage} V")
print(f"Device with Lowest Voltage: {lowest_voltage_device}")
print(f"Unique Device Types: {unique_device_types}")
print(f"Number of Unique Devices: {len(unique_device_ids)}")