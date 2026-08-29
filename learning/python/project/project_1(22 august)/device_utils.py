def calculate_failed_test(total_test, passed_test):
    failed_test = total_test - passed_test
    return failed_test

def calculate_power(voltage, current):
    power = voltage * current
    return power

def calculate_pass_percentage(passed_test, total_test):
    pass_percentage = (passed_test / total_test) * 100 if total_test > 0 else 0
    return pass_percentage

def validate_voltage(voltage, minimum_voltage, maximum_voltage):
    if minimum_voltage <= voltage <= maximum_voltage:
        voltage_status = "PASS"
    else:
        voltage_status = "FAIL"
    return voltage_status

def validate_current(current, maximum_current):
    if current < maximum_current:
        current_status = "PASS"
    else:
        current_status = "FAIL"
    return current_status

def validate_temperature(temperature, minimum_temperature, maximum_temperature):
    if minimum_temperature <= temperature <= maximum_temperature:
        temperature_status = "PASS"
    else:
        temperature_status = "FAIL"
    return temperature_status

def determine_overall_status(voltage_status, current_status, temperature_status, power, pass_percentage):
    if voltage_status == "PASS" and current_status == "PASS" and temperature_status == "PASS"  and power < 10 and pass_percentage >= 95:
        overall_status = "PASS" 
    else:
        overall_status = "FAIL"
    return overall_status

print(validate_voltage(4.8, 3, 5.5))
print(validate_voltage(3, 3, 5.5))
print(validate_voltage(5.6, 3, 5.5))
print(validate_current(5, 10))
print(validate_current(10, 10))
print(validate_current(11, 10))
print(validate_temperature(25, 0, 70))
print(validate_temperature(0, 0, 70))
print(validate_temperature(71, 0, 70))