temperature = float(input("temperature: "))
humidity = float(input("Humidity: "))
voltage = float(input("Voltage: "))
current  = float(input("Current: "))

print("==== Device Information ====")
print(f"Temperature: {type(temperature)} °C\nHumidity: {type(humidity)} %\nVoltage: {type(voltage)} V\nCurrent: {type(current)} A")
print(f"Temperature: {temperature} °C\nHumidity: {humidity} %\nVoltage: {voltage} V\nCurrent: {current} A")
print("============================")