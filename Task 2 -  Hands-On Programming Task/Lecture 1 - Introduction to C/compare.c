#include <stdio.h>

int int_input(char str[]) {
    int answer;
    
    printf("%s", str);
    scanf("%d", &answer);

    return answer;
}

int main(void) {
    int x = int_input("What is the value of X? ");
    int y = int_input("What is the value of Y? ");

    if (x < y) {
        printf("X is less than Y\n");
    } else if (x > y) {
        printf("X is greater than Y\n");
    } else {
        printf("X and Y are same\n");
    }

    return 0;
}
