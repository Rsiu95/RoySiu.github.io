#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

float calc_hours(int hours[], int weeks, char output);

int main(void)
{
    int weeks = get_int("Number of weeks taking CS50: ");
    int hours[weeks];

    for (int i = 0; i < weeks; i++)
    {
        hours[i] = get_int("Week %i HW Hours: ", i);
    }

    char output;
    do
    {
        output = toupper(get_char("Enter T for total hours, A for average hours per week: "));
    }
    while (output != 'T' && output != 'A');

    printf("%.1f hours\n", calc_hours(hours, weeks, output));
}

// TODO: complete the calc_hours function
float calc_hours(int hours[], int weeks, char output)
{
    int totalHours = 0;

    // Calculate the total hours
    for (int i = 0; i < weeks; i++)
    {
        totalHours += hours[i];
    }

    if (output == 'T')
    {
        return totalHours;
    }
    else if (output == 'A')
    {
        // Calculate average hours per week
        return (float)totalHours / weeks;
    }
    else
    {
        printf("Invalid input. Please enter 'T' for total hours or 'A' for average hours per week.\n");
        // If invalid input, return -1 to indicate an error
        return -1;
    }
}