#include <stdio.h>
#include <cs50.h>
#include <string.h>

void print_column(int Height);

int main(void) {

    int Height = get_int("Height: ");
    print_column(Height);

}


void print_column(int height)
{
    for (int i = 0; i < height; i++)
    {
        printf("#\n");
    }
}
