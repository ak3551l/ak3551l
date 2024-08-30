#include <stdio.h>
#include <cs50.h>

int main (void) {
    char c = get_char("Do you agree? ");

    if (c  == 'Y' || c == 'y') {
        printf("Agreed.\n");
    }

    if (c == 'N' || c == 'n') {
        printf("Not Agreed.\n");
    }
}
