#include <cs50.h>
#include <stdio.h>
#include <string.h>

/*

Not going to bother commenting all the code, since it's basically a copy and paste of each for loop/if statement
Probably could've put into a function, but I didn't do it and just brute forced my solution.

*/


int main(void)
{
    long num;
    int digit = 2;

    // Get user input for a Credit card number
    do
    {
        num = get_long("Number: ");
    }
    while (num < 1);

    // initiate a string of length 256, however probably dont need this many
    char str[256];

    // Converts the long to a string for easier manipulation, but uses more memory
    sprintf(str, "%ld", num);

    // Checks if this is a Mastercard
    if ((strlen(str) == 16 && str[0] == '5' && (str[1] == '1' || str[1] == '2' || str[1] == '3' || str[1] == '4' || str[1] == '5')))
    {
        // initialise the first check of Luhn's algorithm
        int second_to_last = 0;

        // initialise the variable for the numbers that weren't multiplied by 2
        int remaining = 0;

        // increment through the string
        for (int n = 0; n < strlen(str) ; n++)
        {

            // This checks every even position since we know the length of the 16 digit card will go from 0 > 15, hence index 0, 2, 4, ..., 14
            if (n % 2 == 0)
            {
                // Convert the string back to an int
                int temp = str[n] - '0';

                // check if the multiplied value is a length of 2 digits or more
                if (2 * temp > 9)
                {
                    // This initialises an string of length 3, now I'm not super familiar with C but it will overflow if I try to initialise it at length 2... as it would return "10d" as an example if str[n] = '5'
                    // unsure on this behaviour, I'll need to look into this more
                    char prod[3];
                    sprintf(prod, "%id", 2 * temp);

                    // add these together and update the initialised "second_to_last" variable
                    second_to_last = second_to_last + (prod[0] - '0') + (prod[1] - '0');
                }

                // skips the if statement and increment second_to_last if it's just a single digit.
                second_to_last = second_to_last + 2 * temp;
            }
            else
            {
                // Add the remaining values
                remaining = remaining + str[n] - '0';
            }
        }

        // Check the total of remaining and second_to_last before checking if it ends with a 0
        int check_sum = remaining + second_to_last;

        // Here we know that anything %10 will return anything BUT a 0 if it doesn't end in 0.
        if (check_sum % 10 == 0)
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("Invalid\n");
        }
    }
    else if ((strlen(str) == 13 || strlen(str) == 16) && str[0] == '4')
    {
        if (strlen(str) == 16)
        {
            int second_to_last = 0;
            int remaining = 0;
            for (int n = 0; n < strlen(str) ; n++)
            {
                if (n % 2 == 0)
                {
                    int temp = str[n] - '0';
                    if (2 * temp > 9)
                    {
                        char prod[3];
                        sprintf(prod, "%id", 2 * temp);
                        second_to_last = second_to_last + (prod[0] - '0') + (prod[1] - '0');
                    }
                    second_to_last = second_to_last + 2 * temp;
                }
                else
                {
                    remaining = remaining + str[n] - '0';
                }
            }
            int check_sum = remaining + second_to_last;
            if (check_sum % 10 == 0)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        if (strlen(str) == 13)
        {
            int second_to_last = 0;
            int remaining = 0;
            for (int n = 0; n < strlen(str) ; n++)
            {
                if (n % 2 != 0)
                {
                    int temp = str[n] - '0';
                    if (2 * temp > 9)
                    {
                        char prod[3];
                        sprintf(prod, "%id", 2 * temp);
                        second_to_last = second_to_last + (prod[0] - '0') + (prod[1] - '0');
                    }
                    second_to_last = second_to_last + 2 * temp;
                }
                else
                {
                    remaining = remaining + str[n] - '0';
                }
            }
            int check_sum = remaining + second_to_last;
            if (check_sum % 10 == 0)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
    }
    else if (strlen(str) == 15 && str[0] == '3' && (str[1] == '4' || str[1] == '7'))
    {
        int second_to_last = 0;
        int remaining = 0;
        for (int n = 0; n < strlen(str) ; n++)
        {
            if (n % 2 != 0)
            {
                int temp = str[n] - '0';
                if (2 * temp > 9)
                {
                    char prod[3];
                    sprintf(prod, "%id", 2 * temp);
                    second_to_last = second_to_last + (prod[0] - '0') + (prod[1] - '0');
                }
                second_to_last = second_to_last + 2 * temp;
            }
            else
            {
                remaining = remaining + str[n] - '0';
            }
        }
        int check_sum = remaining + second_to_last;
        if (check_sum % 10 == 0)
        {
            printf("AMEX\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
