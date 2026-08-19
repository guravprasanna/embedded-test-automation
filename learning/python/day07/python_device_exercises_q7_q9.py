# Python Exercise Q7, Q8, Q9
# Device Test Analyzer / Multi-Device Analyzer / Firmware Test Summary


# =========================
# Q7 - Device Test Analyzer
# =========================

device_id = input("Enter The Device ID:")

device_type = input("Enter Device Type:")

total_test = int(input("Enter Total Test:"))

passed_test = int(input("Enter Passed Test:"))

operating_voltage = float(input("Enter Operating Voltage:"))

operating_current = float(input("Enter Operating Current:"))

failed_test = total_test - passed_test

power_consumption = operating_voltage * operating_current

if total_test == 0 and passed_test == 0:
    passed_percentage = 0
    print("No tests were conducted.")

elif total_test == 0 and passed_test > 0:
    passed_percentage = 0
    print("Invalid input. Passed tests cannot exist when total tests are 0.")

elif total_test > 0 and passed_test == 0:
    passed_percentage = 0
    print("No tests were passed.")

elif total_test < 0 or passed_test < 0:
    passed_percentage = 0
    print("Invalid input. Total tests and passed tests cannot be negative.")

elif passed_test > total_test:
    passed_percentage = 0
    print("Invalid input. Passed tests cannot exceed total tests.")

else:
    passed_percentage = (passed_test / total_test) * 100

print("==== Device Information ====")

print(
    f"Device ID: {device_id}\n"
    f"Device Type: {device_type}\n"
    f"Total Tests: {total_test}\n"
    f"Passed Tests: {passed_test}\n"
    f"Failed Tests: {failed_test}\n"
    f"Power Consumption: {power_consumption} W\n"
    f"Passed Percentage: {passed_percentage:.2f}%"
)

if (
    total_test == passed_test
    and 3 <= operating_voltage <= 5.5
    and power_consumption < 10
    and total_test > 0
    and passed_test > 0
):
    print("Device is Passed")
else:
    print("Device is Failed")

print("============================")


# =========================
# Q8 - Multi-Device Test Analyzer
# =========================

def create_device():
    device = {
        "device_id": "",
        "device_type": "",
        "voltage": 0,
        "current": 0,
        "total_test": 0,
        "passed_test": 0,
        "power": 0,
        "pass_percentage": 0
    }

    device["device_id"] = input("Enter Device ID: ")
    device["device_type"] = input("Enter Device Type: ")
    device["voltage"] = float(input("Enter Voltage: "))
    device["current"] = float(input("Enter Current: "))
    device["total_test"] = int(input("Enter Total Test: "))
    device["passed_test"] = int(input("Enter Passed Test: "))

    device["power"] = device["voltage"] * device["current"]

    device["pass_percentage"] = (
        (device["passed_test"] / device["total_test"]) * 100
        if device["total_test"] > 0
        and device["passed_test"] > 0
        and device["total_test"] >= device["passed_test"]
        else 0
    )

    return device


highest_power = None
lowest_pass_percentage = None

number_of_devices = int(input("How many devices? "))

if number_of_devices <= 0:
    print("Number of devices must be greater than 0.")
    exit()

devices = []

for i in range(number_of_devices):
    device = create_device()
    devices.append(device)

print("========== DEVICE TEST SUMMARY ==========")

for device in devices:
    print(
        f"Device: {device['device_id']}\n"
        f"Type: {device['device_type']}\n"
        f"Power: {device['power']}W\n"
        f"Pass Percentage: {device['pass_percentage']}%\n"
        f"Test Result: {'PASS' if device['total_test'] == device['passed_test'] and 3 <= device['voltage'] <= 5.5 and device['power'] < 10 and device['total_test'] > 0 and device['passed_test'] > 0 else 'FAIL'}\n"
    )

print("==========================================")

print(f"Total Devices Tested: {len(devices)}")

print(
    f"Devices Passed: "
    f"{sum(1 for device in devices if device['total_test'] == device['passed_test'] and 3 <= device['voltage'] <= 5.5 and device['power'] < 10 and device['total_test'] > 0 and device['passed_test'] > 0)}"
)

print(
    f"Devices Failed: "
    f"{sum(1 for device in devices if device['total_test'] != device['passed_test'] or not (3 <= device['voltage'] <= 5.5) or device['power'] >= 10 or device['total_test'] <= 0 or device['passed_test'] <= 0)}"
)

for device in devices:
    power = device["power"]

    if highest_power is None or power >= highest_power:
        highest_power = power
        highest_power_device = device["device_id"]

for device in devices:
    pass_percentage = device["pass_percentage"]

    if lowest_pass_percentage is None or pass_percentage <= lowest_pass_percentage:
        lowest_pass_percentage = pass_percentage
        lowest_pass_device = device["device_id"]

overall_pass_percentage = (
    sum(device["passed_test"] for device in devices)
    / sum(device["total_test"] for device in devices)
    * 100
    if sum(device["total_test"] for device in devices) > 0
    else 0
)

print(f"Device with Highest Power: {highest_power_device} ({highest_power}W)")
print(f"Device with Lowest Pass Percentage: {lowest_pass_device} ({lowest_pass_percentage}%)")
print(f"Overall Test Pass Percentage: {overall_pass_percentage:.2f}%")


# =========================
# Q9 - Firmware Test Summary
# =========================

def create_firmware_device():
    device = {
        "device_id": "",
        "device_type": "",
        "firmware_version": "",
        "voltage": 0,
        "current": 0,
        "total_functional_test": 0,
        "passed_functional_test": 0,
        "failed_functional_test": 0,
        "power": 0,
        "pass_percentage": 0,
        "temperature": 0,
        "voltage_status": "",
        "current_status": "",
        "temperature_status": "",
        "overall_status": ""
    }

    device["device_id"] = input("Enter Device ID: ")
    device["device_type"] = input("Enter Device Type: ")
    device["firmware_version"] = input("Enter Firmware Version: ")
    device["voltage"] = float(input("Enter Voltage: "))
    device["current"] = float(input("Enter Current: "))
    device["total_functional_test"] = int(input("Enter Total Functional Test: "))
    device["passed_functional_test"] = int(input("Enter Passed Functional Test: "))
    device["temperature"] = float(input("Enter Temperature: "))

    device["failed_functional_test"] = (
        device["total_functional_test"] - device["passed_functional_test"]
    )

    device["power"] = device["voltage"] * device["current"]

    device["pass_percentage"] = (
        (device["passed_functional_test"] / device["total_functional_test"]) * 100
        if device["total_functional_test"] > 0
        else 0
    )

    if 3 <= device["voltage"] <= 5.5:
        device["voltage_status"] = "PASS"
    else:
        device["voltage_status"] = "FAIL"

    if device["current"] < 10:
        device["current_status"] = "PASS"
    else:
        device["current_status"] = "FAIL"

    if 0 <= device["temperature"] <= 70:
        device["temperature_status"] = "PASS"
    else:
        device["temperature_status"] = "FAIL"

    if (
        device["voltage_status"] == "PASS"
        and device["current_status"] == "PASS"
        and device["temperature_status"] == "PASS"
        and device["power"] < 10
        and device["pass_percentage"] >= 95
    ):
        device["overall_status"] = "PASS"
    else:
        device["overall_status"] = "FAIL"

    return device


highest_power = None
lowest_pass_percentage = None

number_of_devices = int(input("How many devices? "))

if number_of_devices <= 0:
    print("Number of devices must be greater than 0.")
    exit()

devices = []

for i in range(number_of_devices):
    device = create_firmware_device()
    devices.append(device)

print("========== FIRMWARE RELEASE SUMMARY ==========")

for device in devices:
    print(
        f"Device ID: {device['device_id']}\n"
        f"Device Type: {device['device_type']}\n"
        f"Firmware Version: {device['firmware_version']}\n"
        f"Total Functional Tests: {device['total_functional_test']}\n"
        f"Total Passed Tests: {device['passed_functional_test']}\n"
        f"Failed Tests: {device['failed_functional_test']}\n"
        f"Power: {device['power']}W\n"
        f"Pass Percentage: {device['pass_percentage']:.2f}%\n"
        f"Voltage Status: {device['voltage_status']}\n"
        f"Current Status: {device['current_status']}\n"
        f"Temperature Status: {device['temperature_status']}\n"
        f"Overall Device Status: {device['overall_status']}\n"
    )

print("==========================================")

print(f"Total Devices Tested: {len(devices)}")

print(
    f"Devices Passed: "
    f"{sum(1 for device in devices if device['overall_status'] == 'PASS')}"
)

print(
    f"Devices Failed: "
    f"{sum(1 for device in devices if device['overall_status'] == 'FAIL')}"
)

for device in devices:
    power = device["power"]

    if highest_power is None or power >= highest_power:
        highest_power = power
        highest_power_device = device["device_id"]

for device in devices:
    pass_percentage = device["pass_percentage"]

    if lowest_pass_percentage is None or pass_percentage <= lowest_pass_percentage:
        lowest_pass_percentage = pass_percentage
        lowest_pass_device = device["device_id"]

overall_pass_percentage = (
    sum(device["passed_functional_test"] for device in devices)
    / sum(device["total_functional_test"] for device in devices)
    * 100
    if sum(device["total_functional_test"] for device in devices) > 0
    else 0
)

print(f"Device with Highest Power: {highest_power_device} ({highest_power}W)")
print(f"Device with Lowest Pass Percentage: {lowest_pass_device} ({lowest_pass_percentage}%)")
print(f"Overall Test Pass Percentage: {overall_pass_percentage:.2f}%")

release_status = all(device["overall_status"] == "PASS" for device in devices)

print(f"Firmware Release Status: {'PASS' if release_status else 'FAIL'}")

print("==========================================")
