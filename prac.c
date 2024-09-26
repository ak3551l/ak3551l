#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(void) {
    int *x;
    int *y;
    x = malloc(sizeof(int));

    *x = 42;
    *y = *x;
    printf("%i \n", y);

    *y = 13;
    printf("%i \n", y);

    free(x);

}
