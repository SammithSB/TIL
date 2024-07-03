use std::f64;

fn is_prime(n: i32) -> bool {
    if n <= 1 {
        return false;
    }
    let sqrt_n = (n as f64).sqrt() as i32;
    for i in 2..=sqrt_n {
        if n % i == 0 {
            return false;
        }
    }
    true
}

fn is_caboose(n: i32) -> bool {
    for i in 1..=n {
        let x = i * i - i + 41;
        if !is_prime(x) {
            return false;
        }
    }
    true
}

fn caboose_prime_ratio(n: i32) -> f64 {
    let mut prime_count = 0;
    for i in 1..=n {
        let x = i * i - i + 41;
        if is_prime(x) {
            prime_count += 1;
        }
    }
    prime_count as f64 / n as f64
}

fn main() {
    let n = 100;
    for i in 1..n {
        if is_caboose(i) {
            println!("{} is Caboose", i);
        } else {
            println!("{} is not Caboose", i);
        }
        println!("Caboose ratio for {} is {:.2}", i, caboose_prime_ratio(i));
    }
}
