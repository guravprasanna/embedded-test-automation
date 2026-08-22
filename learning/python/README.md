Python Learning

This section documents my progression in Python, starting from programming fundamentals and progressing toward embedded test automation.

Learning Path

Day 01 — Variables, Data Types and Input/Output

Variables

Strings

Integers

Floats

Booleans

input()

Type conversion

f-strings

Basic calculations

Day 02 — Conditional Logic

if

elif

else

Comparison operators

Logical operators

Nested conditions

Day 03 — Loops and Functions

while loops

for loops

range()

break

continue

Functions

Function parameters

return

Reusable functions

Day 04 — Flow Control and Unit Converter

if / elif / else

while loops

for loops

Functions

Function parameters and return values

Nested menu logic

User input

Type conversion

Built a device value converter

Voltage conversion: V ↔ mV

Current conversion: A ↔ mA

Resistance conversion: Ω ↔ kΩ

Power conversion: W ↔ kW

Day 05 — Data Structures and Device Data Modeling

Lists

List indexing

.append()

Tuples

Tuple indexing

Sets

.add()

len()

Dictionaries

Nested dictionaries

Lists of dictionaries

for loops with device data

Modeling sensor/device information

Extracting unique device IDs

Extracting unique device types

Finding highest temperature

Finding lowest voltage

Comparing sensor values

Built an IoT device data model

Saturday — Device Test CLI Project

Built a menu-driven Device Test CLI for embedded-device validation.

Features:

Add devices

View stored devices

Run device validation tests

Generate test reports

View previous test reports

Firmware release history

Device voltage validation

Device current validation

Device temperature validation

Power consumption calculation

Functional test pass percentage

Overall device PASS/FAIL status

Firmware release PASS/FAIL decision

Separate device data and test-report data

In-memory device and test-report storage

Project structure:

projects/
└── device_test_cli/
    └── device_test_cli.py

Sunday — Python Revision Exercises

Revised Python fundamentals

Practiced lists and dictionaries

Practiced loops

Practiced functions

Practiced conditional logic

Worked with device test data

Practiced dictionary manipulation

Practiced reusable functions

Debugged device validation logic

Strengthened problem-solving through independent exercises

Day 11 — Modules and Imports

Understanding Python modules

Understanding why modules are needed

Creating custom Python modules

Using import module

Using from module import function

Understanding module namespaces

Importing multiple functions from a module

Creating reusable utility functions

Separating reusable logic from application logic

Identifying responsibilities inside an existing function

Refactoring an existing project using modules

Created device_utils.py

Imported device_utils into the Device Test CLI

Moved reusable device-test logic from run_test() into device_utils.py

Verified the refactored CLI after modularization

Device utility functions:

calculate_failed_test()

calculate_power()

calculate_pass_percentage()

validate_voltage()

validate_current()

validate_temperature()

determine_overall_status()

Day 11 project structure:

day11/
└── project/
    ├── device_test_cli.py
    └── device_utils.py

Upcoming Topics

Exception handling

File handling

Object-oriented programming

JSON

API interaction

pytest

Serial/UART automation

MQTT automation

Modbus automation

Goal

Build a strong Python foundation and apply it to practical embedded-device testing and automation.
