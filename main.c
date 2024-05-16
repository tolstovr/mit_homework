#include <stdio.h>

void fib(int n) {
    int a = 0, b = 1;
    for (int i = 0; i < n; ++i) {
        printf("%d\n", a);
        int temp = a;
        a = b;
        b = temp + b;
    }
}

int main() {
    int n;
    printf("%s\n", "n:");
    scanf("%d", &n);
    fib(n);
    return 0;
}