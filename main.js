const fib = (n) => (n <= 2 ? n - 1 : fib(n - 1) + fib(n - 2))

const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.question("n: ", (n) => {
    console.log(`fib(${n}) = ${fib(parseInt(n))}`)
    rl.close()
})