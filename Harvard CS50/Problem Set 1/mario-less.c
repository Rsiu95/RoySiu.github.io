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
        for (int space = 1; space < size - row; space++)
        {
            printf(" ");
        }
        for (int hash = 0; hash < row + 1; hash ++)
        {
            printf("#");
        }

        printf("\n");
    }
}