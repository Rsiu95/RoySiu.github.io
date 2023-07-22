// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Function prototype to replace vowels with numbers
string replace(string input);

int main(int argc, string argv[])
{
    // Check if the program is executed with exactly one command-line argument
    if (argc != 2)
    {
        printf("Usage: %s word\n", argv[0]);
        return 1; // Return an error code
    }

    string convertedWord = replace(argv[1]);
    printf("%s\n", convertedWord);

    return 0;
}

// Function to replace vowels with numbers in the input string
string replace(string input)
{
    // Create a new string to store the converted word
    string convertedWord = input;

    // Iterate through each character in the input string
    for (int i = 0, n = strlen(input); i < n; i++)
    {
        char currentChar = input[i];

        // Use the switch statement to replace vowels with numbers
        switch (currentChar)
        {
            case 'a':
            case 'A':
                convertedWord[i] = '6';
                break;
            case 'e':
            case 'E':
                convertedWord[i] = '3';
                break;
            case 'i':
            case 'I':
                convertedWord[i] = '1';
                break;
            case 'o':
            case 'O':
                convertedWord[i] = '0';
                break;
            // For 'u' or any other character, do nothing
            default:
                break;
        }
    }

    return convertedWord;
}

