#include <stdio.h>
#include <cs50.h>


int main (int argc, string argv[]) {

    if (argc != 2){
        printf("Missing command line arguments\n");
        return 1;
    }

    printf("%s\n", argv[1]);
    return 0;

}


