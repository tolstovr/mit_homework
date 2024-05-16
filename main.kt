fun fib(n: Int): Int {
    return if (n <= 2) {
        n - 1
    } else {
        fib(n - 1) + fib(n - 2)
    }
}

fun main() {
    print("n: ")
    val n = readLine()!!.toInt()
    println("fib($n) = ${fib(n)}")
}