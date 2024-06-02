#include <cs50.h>
#include <stdio.h>

int add(int a, int b);


int main(void)
{
    int x = get_int("Value of X: ");
    int y = get_int("Value of y: ");

    printf("Answer: %i\n", add(x, y));

}

int add(int a, int b)
{
    int z = a + b;
    return z;
}
