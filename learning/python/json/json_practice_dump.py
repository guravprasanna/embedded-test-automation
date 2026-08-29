import json
devices = []

def add_device():
    device = {
        "device_id": "",
        "device_type": "",
        "firmware_version": "",
        "voltage": 0,
        "current": 0,
        "total_test": 0,
        "passed_test": 0,
        "temperature": 0
    }

    device["device_id"] = input("Enter Device ID: ")
    device["device_type"] = input("Enter Device Type: ")
    device["firmware_version"] = input("Enter Firmware Version: ")
    device["voltage"] = float(input("Enter Voltage: "))
    device["current"] = float(input("Enter Current: "))
    device["total_test"] = int(input("Enter Total Functional Test: "))
    device["passed_test"] = int(input("Enter Passed Functional Test: "))
    device["temperature"] = float(input("Enter Temperature: "))

    return device

def main():
    while True:
        print("====================\n DEVICE TEST CLI \n=====================")
        print("1. Add Devices")

        choice = input("Enter your choice: ")

        if choice == "1":
            device = add_device()
            devices.append(device)
            print("Device added successfully.")
        elif choice == "exit":
            print("Exit")
            break
        else:
            print("Invalid choice. Please try again.")
main()


output_1 = open("output_1.json", "w")
json.dump(devices, output_1, indent = 4)
output_1.close()