def unit_to_milliunit(value):
    return value * 1000

def milliunit_to_unit(value):
    return value / 1000
choice_1 = 0
while choice_1 != 5:   
    print("DEVICE VALUE CONVERTER \n 1. Voltage \n 2. Current \n 3.Resistance \n 4.Power \n 5. Exit")
    choice_1 = int(input("Select an option: "))
    if choice_1 == 1:
        print("Voltage Selected")
        print("1. Volts to Millivolts \n 2. Millivolts to Volts")
        choice_2 = int(input("Select a conversion: "))
        if choice_2 == 1:
            voltage = float(input("Enter voltage in volts: "))
            result = unit_to_milliunit(voltage)
            print(f"Voltage in millivolts: {result} mV")
        elif choice_2 == 2:
            voltage = float(input("Enter voltage in millivolts: "))
            result = milliunit_to_unit(voltage)
            print(f"Voltage in volts: {result} V")
    elif choice_1 == 2:
        print("Current Selected")
        print("1. Amperes to Milliamperes \n 2. Milliamperes to Amperes")
        choice_2 = int(input("Select a conversion: "))
        if choice_2 == 1:
            current = float(input("Enter current in amperes: "))
            result = unit_to_milliunit(current)
            print(f"Current in milliamperes: {result} mA")
        elif choice_2 == 2:
            current = float(input("Enter current in milliamperes: "))
            result = milliunit_to_unit(current)
            print(f"Current in amperes: {result} A")
    elif choice_1 == 3:
        print("Resistance Selected")
        print("1. Kiloohms to Ohms \n 2. Ohms to Kiloohms")
        choice_2 = int(input("Select a conversion: "))
        if choice_2 == 1:
            resistance = float(input("Enter resistance in kiloohms: "))
            result = unit_to_milliunit(resistance)
            print(f"Resistance in Ohms: {result} Ω")
        elif choice_2 == 2:
            resistance = float(input("Enter resistance in ohms: "))
            result = milliunit_to_unit(resistance)
            print(f"Resistance in Kiloohms: {result} kΩ")
    elif choice_1 == 4:
        print("Power Selected")
        print("1. Kilowatts to Watts \n 2. Watts to Kilowatts")
        choice_2 = int(input("Select a conversion: "))
        if choice_2 == 1:
            power = float(input("Enter power in kilowatts: "))
            result = unit_to_milliunit(power)
            print(f"Power in Watts: {result} W")
        elif choice_2 == 2:
            power = float(input("Enter power in watts: "))
            result = milliunit_to_unit(power)
            print(f"Power in Kilowatts: {result} kW")
    elif choice_1 == 5:
        print("Exiting the program.")