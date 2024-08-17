/*
    PH04082024: This programme was written
    to improve my skills in C programming with
    some known keywords and approach of
    calculating two numbers
*/

#include <stdio.h>

int add(int a, int b) {
    return a+b;
}

int subtract(int a, int b) {
    return a-b;
}

int multiply(int a, int b) {
    return a*b;
}

double divide(int a, int b) {
    return (double)a / b;
}

int main(void) {
    int x, y;
    double output;
    char operator;

    printf("Enter an expression to calculate (Ex. 3 + 2): ");
    scanf("%d %c %d", &x, &operator, &y);

    switch (operator) {
        case '+':
            output = add(x, y);
            printf("\nTHE ANSWER IS: %d\n", (int)output);
            break;
        case '-':
            output = subtract(x, y);
            printf("\nTHE ANSWER IS: %d\n", (int)output);
            break;
        case '*':
            output = multiply(x, y);
            printf("\nTHE ANSWER IS: %d\n", (int)output);
            break;
        case '/':
            if (y == 0) {
                printf("Error: Division by zero\n");
                return 1;
            }

            output = divide(x, y);
            printf("\nTHE ANSWER IS: %.2f\n", output);
            break;
        default:
            printf("Invalid operator\n");
            return 1;
    }

    printf("\nTHE ANSWER IS: %.5f\n", (float) output);
}