#include <stdio.h>
#include <string.h>
#include <cs50.h>


typedef struct{
        string name;
        string number;
    }

    person;

int main (void) {

    person people[3];

    people[0].name = "Carter";
    people[0].number = "+91-8860897365";

    people[1].name = "David";
    people[1].number = "+91-8799398401";

    people[2].name = "John";
    people[2].number = "+91-7799798331";

    string name = get_string("Name: ");

    for (int i=0; i < 3; i++) {
        if (strcmp(people[i].name, name) == 0) {
            printf("Found\n");
            return 0;
        }
    }



}
