#include <cs50.h>
#include <stdio.h>
#include <string.h>

void print_column(int height);

int main(void)
{
    const int N = 3;
    int Score[N];

    for (int i=0; i < 3; i++)
    {
        Score[i] = get_int("Score: ");
    }

    printf("Average: %f\n", (Score[0] + Score[1] + Score[2]) / 3.0);
}
