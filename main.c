#include <stdio.h>

int fib(int n) {
    if (n <= 2) return n - 1;
    else return fib(n - 1) + fib(n - 2);
}

int main() {
    int n;
    printf("n: ");
    scanf("%d", &n);
    printf("fib(%d) = %d\n", n, fib(n));
    return 0;
}