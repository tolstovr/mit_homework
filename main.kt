fun fib(n: Int) {
    var a = 0
    var b = 1
    repeat(n) {
        println(a)
        val temp = a
        a = b
        b += temp
    }
}

fun main() {
    print("n: ")
    val n = readLine()!!.toInt()
    fib(n)
}