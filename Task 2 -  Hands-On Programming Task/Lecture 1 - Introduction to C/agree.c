#include <stdio.h>

char str_input(char str[]) {
    char answer;

    printf("%s", str);
    scanf("%s", &answer);

    return answer;
}

int main(void) {
    char agree = str_input("Do you agree ? ");

    if (agree == 'y' || agree == 'Y') {
        printf("You agreed !!\n");
    } else if (agree == 'n' || agree == 'N') {
        printf("You disagreed !!\n");
    }
}