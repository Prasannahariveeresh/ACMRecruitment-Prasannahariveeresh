#include <stdio.h>

float avg(int length, int array[]) {
    float sum = 0;

    for (int i=0; i < length; i++) {
        sum += array[i];
    }

    return sum / (float) length;
}

int int_input(char str[]) {
    int answer;

    printf("%s", str);
    scanf("%i", &answer);

    return answer;
}

int main(void) {
    int n = int_input("Enter number of records: ");
    int scores[n];

    for (int i=0; i < n; i++) {
        scores[i] = int_input("Enter the score of student: ");
    }

    float average = avg(n, scores);
    printf("The average score of the student = %f\n", average);
}