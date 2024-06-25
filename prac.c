#include <stdio.h>
#include <cs50.h>

int main(void) {
    int x = get_int("X: ");
    int y = get_int("Y: ");



    if (x > y) {
        printf("X is greater than Y.\n");
    }

    if (x < y) {
        printf("X is less than Y.\n");
    }

    else {
        printf("X is equal to Y.\n");
    }
}

