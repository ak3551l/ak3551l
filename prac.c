#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void) {

    string phrase = get_string("Phrase: ");
    int length = strlen(phrase);

    for (int i = 0; i < length; i++)
    {
        printf("%s\n", phrase[i]);
    }
}

