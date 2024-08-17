#include <stdio.h>
#include <string.h>
#include <ctype.h>

void str_input(char answer[], int size) {
    printf("Enter your string: ");
    fgets(answer, size, stdin);

    size_t len = strlen(answer);
    if (len > 0 && answer[len - 1] == '\n') {
        answer[len - 1] = '\0';
    }
}

int main(void) {
    char str[256];
    str_input(str, sizeof(str));

    for (int i = 0; i < strlen(str); i++) {
        printf("%c", toupper(str[i]));
    }
    printf("\n");
}