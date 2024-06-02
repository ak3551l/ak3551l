#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int counter = 10;
    while (counter > 0)
    {
        printf("%i\n", counter);
        counter -= 1;
    }
    printf("Hello, Abhijeet\n");
}
