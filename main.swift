print("n: ")
if let n = readLine(), let nInt = Int(n) {
    var a = 0
    var b = 1
    for _ in 0..<nInt {
        print("\(a)\n")
        let temp = a
        a = b
        b = temp + b
    }
}