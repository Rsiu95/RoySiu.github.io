// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    bool hasLowerCase = false;
    bool hasUpperCase = false;
    bool hasNumber = false;
    bool hasSymbol = false;

    // Iterate through each character in the password
    for (int i = 0; password[i] != '\0'; i++)
    {
        char currentChar = password[i];

        // Check if the character is a lowercase letter
        if (islower(currentChar))
        {
            hasLowerCase = true;
        }
        // Check if the character is an uppercase letter
        else if (isupper(currentChar))
        {
            hasUpperCase = true;
        }
        // Check if the character is a digit (number)
        else if (isdigit(currentChar))
        {
            hasNumber = true;
        }
        // Check if the character is a symbol (neither letter nor number)
        else if (!isalnum(currentChar))
        {
            hasSymbol = true;
        }

        // If all criteria are met, return true
        if (hasLowerCase && hasUpperCase && hasNumber && hasSymbol)
        {
            return true;
        }
    }

    // If any of the criteria is not met, return false
    return false;
}
