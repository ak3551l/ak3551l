// Debug the code below to solve the problem

#include <stdio.h>

int main() {
    int N, sum = 0;
    scanf("%d", &N);
    int i = 0;

    while (i <= N) {
        sum += i;
        i ++;
    };

    printf("%d", sum);
    return 0;
}
