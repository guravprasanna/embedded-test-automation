temperature = float(input("temperature: "))
humidity = float(input("Humidity: "))
voltage = float(input("Voltage: "))
current  = float(input("Current: "))
power = voltage * current
average = (temperature + humidity) / 2

print("==== Device Information ====")
print(f"Temperature: {temperature} °C\nHumidity: {humidity} %\nVoltage: {voltage} V\nCurrent: {current} A\n\n\nPower: {power} W\nAverage: {average}")
print("============================")