#include <stdio.h>
#include <cs50.h>

int main(void) {
    int x = get_int("X: \n");
    int y = get_int("Y: \n");

    if (x > y) {
        printf("x is greater than y.\n");
    }

    elif (x < y) {
        printf("x is less than y.\n");
    }
}


