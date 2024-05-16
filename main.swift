func fib(_ n: Int) -> Int {
    if n <= 1 {
        return n
    } else {
        return fib(n - 1) + fib(n - 2)
    }
}

print("n: ", terminator: "")
if let input = readLine(), let n = Int(input) {
    print("fib(\(n)) = \(fib(n))")
}