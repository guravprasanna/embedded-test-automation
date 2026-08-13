#include <stdio.h>
#define MINIMUM_VOLTAGE 120.0f
#define MAXIMUM_VOLTAGE 240.0f

int main(void)
{
    float Operating_Voltage;

    printf("======== Device VOLTAGE TEST =========\n");
    printf("Minimum Voltage: %.2f V\n", MINIMUM_VOLTAGE);
    printf("Maximum Voltage: %.2f V\n\n", MAXIMUM_VOLTAGE);
    printf("Enter the operating voltage of the device: ");
    scanf("%f", &Operating_Voltage);
    printf("Operating Voltage: %.2f V\n", Operating_Voltage);
    return 0;
}