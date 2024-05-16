#include <iostream>
typedef long long int llint;

llint fib(llint n) {
    if (n <= 1) return n;
    else return fib(n - 1) + fib(n - 2);
}

int main() {
    llint n;
    std::cout << "n: ";
    std::cin >> n;
    std::cout << "fib(" << n << ") = " << fib(n) << std::endl;
    return 0;
}