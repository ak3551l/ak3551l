#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void) {

    string phrase = get_string("Phrase: ");
    int length = strlen(phrase);

    for (int i = 0; i < length; i++)
    {
        if (phrase[i] > phrase[i + 1])
        {
            printf("Not in alphabetical order\n");
            return 0;
        }
        else {
            printf("In alphabetical order\n");
            return 0;
        }
    }
}

