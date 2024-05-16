#include <iostream>
typedef long long int llint;

void fib(llint n) {
    int a = 0, b = 1;
    for (int i = 0; i < n; ++i) {
        std::cout << a << std::endl;
        int temp = a;
        a = b;
        b = temp + b;
    }
}

int main() {
    int n;
    std::cout << "n: ";
    std::cin >> n;
    fib(n);
    return 0;
}