#include <stdio.h>
#include <string.h>

void str_input(char answer[], int size) {
    printf("What's your name? ");
    fgets(answer, size, stdin);

    size_t len = strlen(answer);
    if (len > 0 && answer[len - 1] == '\n') {
        answer[len - 1] = '\0';
    }
}

int main(void) {
    char str[256];
    str_input(str, sizeof(str));

    int len = strlen(str);
    printf("Total length of the string is %d\n", len);
}
