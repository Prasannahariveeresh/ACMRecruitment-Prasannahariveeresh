#include <stdio.h>

void meow(int n) {
    for (int j=0; j<n; j++) {
        printf("meow !!\n");
    }
}

int main(void) {
    meow(3);
}