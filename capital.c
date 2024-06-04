#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After: ");

    for (int i=0, n = strlen(s); i < n; i++)
    {
        //If lowercase
        if (s[i] > 'a' && s[i] < 'z')
        {
            printf("%c\n", s[i] - 32);
        }
        else
        {
            printf("%c\n", s[i]);
        }
    }
}
