func fib(_ n: Int) -> Int {
    if n <= 2 {
        return n - 1
    } else {
        return fib(n - 1) + fib(n - 2)
    }
}

print("n: ")
if let input = readLine(), let n = Int(input) {
    print("fib(\(n)) = \(fib(n))")
}