use std::io;

fn fib(n: u32) {
    let (mut a, mut b) = (0, 1);
    for _ in 0..n {
        println!("{}", a);
        let temp = a;
        a = b;
        b = temp + b;
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let n: u32 = input.trim().parse().expect("Please enter a number");
    fib(n);
}