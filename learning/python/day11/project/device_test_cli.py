import device_utils
devices = []
test_reports = []
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

def view_device(devices):
    print("\n========== DEVICES ==========")
    for device in devices:
        print("Viewing devices: ")
        print(f"DEVICE ID: {device["device_id"]}")
        print(f"DEVICE TYPE: {device["device_type"]}")
        print(f"FIRMWARE VERSION: {device["firmware_version"]}")
        print(f"VOLTAGE: {device["voltage"]}")
        print(f"CURRENT: {device["current"]}")
        print(f"TOTAL TEST: {device["total_test"]}")
        print(f"PASSED TEST: {device["passed_test"]}")
        print(f"TEMPERATURE: {device["temperature"]}\n")
    print("=============================")

def run_test(devices):
    for device in devices:
        print(f"{device['device_id']} | {device['device_type']} | {device['firmware_version']}")
    device_id = input("Enter Device ID to test: ")
    for device in devices:
        if device["device_id"] == device_id:
            test_report = {
            "device_id": "",
            "firmware_version": "",
            "total_test": 0,
            "passed_test": 0,
            "power": 0,
            "failed_test": 0,
            "pass_percentage": 0,
            "voltage_status": "",
            "current_status": "",
            "temperature_status": "",
            "overall_status": ""
            }

            test_report["total_test"] = device["total_test"]
            test_report["passed_test"] = device["passed_test"]
            test_report["device_id"] = device["device_id"]
            test_report["firmware_version"] = device["firmware_version"]
            test_report["failed_test"] = device_utils.calculate_failed_test(device["total_test"], device["passed_test"])
            test_report["power"] = device_utils.calculate_power(device["voltage"], device["current"])
            test_report["pass_percentage"] = device_utils.calculate_pass_percentage(device["passed_test"], device["total_test"])
            test_report["voltage_status"] = device_utils.validate_voltage(device["voltage"])
            test_report["current_status"] = device_utils.validate_current(device["current"])
            test_report["temperature_status"] = device_utils.validate_temperature(device["temperature"])
            test_report["overall_status"] = device_utils.determine_overall_status(test_report["voltage_status"], test_report["current_status"], test_report["temperature_status"], test_report["power"], test_report["pass_percentage"])
            print("Device was Found and Test was performed.")
            return test_report
    print("Device not Found.")
    return None

def view_test_reports(test_reports, devices):
    if not test_reports:
        print("No test reports available.\nPlease run a device test first.")
        choice = input("Would you like to run a device test now? (y/n): ")
        if choice == "y":
           report = run_test(devices)
           if report is not None:
            test_reports.append(report)
           view_test_reports(test_reports, devices)
        elif choice == "n":
            return
    else:
        print("\n========== VIEW TEST REPORTS ==========")
        for report in test_reports:
            print("View TEST REPORTS: ")
            print(f"DEVICE ID: {report["device_id"]}")
            print(f"FIRMWARE VERSION: {report["firmware_version"]}")
            print(f"FAILED TEST: {report["failed_test"]}")
            print(f"POWER: {report["power"]}")
            print(f"PASS PERCENTAGE: {report["pass_percentage"]}")
            print(f"VOLTAGE STATUS: {report["voltage_status"]}")
            print(f"CURRENT STATUS: {report["current_status"]}")
            print(f"TEMPERATURE STATUS: {report["temperature_status"]}")
            print(f"OVERALL STATUS: {report["overall_status"]}\n")
        print("=============================")

def firmware_release(test_reports):

    if not test_reports:
        print("No test reports available.")
        print("Please run a device test first.")
        return

    firmware_versions = []

    for report in test_reports:
        if report["firmware_version"] not in firmware_versions:
            firmware_versions.append(report["firmware_version"])

    print("\n========== FIRMWARE RELEASE HISTORY ==========")

    for firmware in firmware_versions:

        total_tests = 0
        passed_tests = 0
        devices_tested = 0
        devices_passed = 0
        devices_failed = 0

        for report in test_reports:

            if report["firmware_version"] == firmware:

                devices_tested += 1
                total_tests += report["total_test"]
                passed_tests += report["passed_test"]

                if report["overall_status"] == "PASS":
                    devices_passed += 1
                else:
                    devices_failed += 1

        overall_pass_percentage = (
            (passed_tests / total_tests) * 100
            if total_tests > 0
            else 0
        )

        if devices_failed == 0 and overall_pass_percentage >= 95:
            release_status = "PASS"
        else:
            release_status = "FAIL"

        print(f"\nFirmware Version: {firmware}")
        print(f"Devices Tested: {devices_tested}")
        print(f"Devices Passed: {devices_passed}")
        print(f"Devices Failed: {devices_failed}")
        print(f"Total Tests: {total_tests}")
        print(f"Passed Tests: {passed_tests}")
        print(f"Overall Pass Percentage: {overall_pass_percentage:.2f}%")
        print(f"Release Status: {release_status}")

    print("==============================================")


def main():
    while True:
        print("====================\n DEVICE TEST CLI \n=====================")
        print("1. Add Devices")
        print("2. View Devices")
        print("3. Run Device Test")
        print("4. View Test Reports")
        print("5. Firmware Release History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            device = add_device()
            devices.append(device)
            print("Device added successfully.")
        elif choice == "2":
            view_device(devices)
        elif choice == "3":
            report = run_test(devices)
            if report is not None:
                test_reports.append(report)
        elif choice == "4":
            view_test_reports(test_reports, devices)
        elif choice == "5":
            firmware_release(test_reports)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()



