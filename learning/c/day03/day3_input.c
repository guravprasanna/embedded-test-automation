#include <stdio.h>

int main(void)
{
    int Device_ID, Total_Tests, Passed_Tests, Failed_Tests;
    float Operating_Voltage, Operating_Current, Power;

    printf("======== Device Information =========\n");
    printf("Enter Device ID: ");
    scanf("%d", &Device_ID);
    printf("Enter Total Tests: ");
    scanf("%d", &Total_Tests);
    printf("Enter Passed Tests: ");
    scanf("%d", &Passed_Tests);
    printf("Enter Operating Voltage: ");
    scanf("%f", &Operating_Voltage);
    printf("Enter Operating Current: ");
    scanf("%f", &Operating_Current);

    Failed_Tests = Total_Tests - Passed_Tests;
    Power = Operating_Voltage * Operating_Current;

    printf("\n======== Device Test Report =========\n");
    printf("Device ID: %d \nTotal tests: %d \nPassed tests: %d \nFailed tests: %d \nOperating Voltage: %.2f V\nOperating Current: %.2f A\nPower: %.2f W", Device_ID, Total_Tests, Passed_Tests, Failed_Tests, Operating_Voltage, Operating_Current, Power);

    return 0;
}