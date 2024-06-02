#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = get_int("Value of X: ");
    int y = get_int("Value of y: ");

    if (x > y)
    {
        printf("x is greater than y.\n");
    }
    else if (x < y)
    {
        printf("x is less than y.\n");
    }
    else
    {
        printf("x is equal to y.\n");
    }
}
