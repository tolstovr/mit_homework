#include <iostream>
typedef long long int llint;

llint fib(llint n) {
    if (n <= 2) return n - 1;
    else return fib(n - 1) + fib(n - 2);
}

int main() {
    llint n;
    std::cout << "n: ";
    std::cin >> n;
    std::cout << "fib(" << n << ") = " << fib(n) << std::endl;
    return 0;
}