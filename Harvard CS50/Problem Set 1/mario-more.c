#include <cs50.h>
#include <stdio.h>

int get_size(void);
void print_grid(int size);

int main(void)
{
    // get size of grid
    int n = get_size();

    // Print grid of size n
    print_grid(n);
}

int get_size(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);
    return n;
}



void print_grid(int size)
{
    for (int row = 0; row < size; row++)
    {
        // Prints the Spaces before the Hashes
        for (int space = 1; space < size - row; space++)
        {
            printf(" ");
        }

        // Prints the Left side of pyramid
        for (int hash = 0; hash < row + 1; hash++)
        {
            printf("#");
        }


        // Prints the spaces inbetween
        for (int space = 0; space < 2; space++)
        {
            printf(" ");
        }

        // Prints the Right side of pyramid
        for (int hash = 0; hash < row + 1; hash++)
        {
            printf("#");
        }

        printf("\n");
    }
}