#include <cs50.h>
#include <stdio.h>
#include <string.h>

void print_column(int height);

int main(void)
{
    int Score[3];

    int Score[0] = get_int("Score: ");
    int Score[1] = get_int("Score: ");
    int Score[2] = get_int("Score: ");

    printf("Average: %f\n", (Score[1] + Score[2] + Score[3]) / 3.0);
}
