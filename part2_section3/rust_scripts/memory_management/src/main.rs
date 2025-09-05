
fn string_lenght(ss: String) -> usize {
    ss.len()
}

fn main() {
    println!("Rust's ownership checking.");
    let s = String::from("Hello");
    let len = string_lenght(s.clone());
    // From here s is no longer valid
    println!("The length of '{}' is {}.", s, len); // Error
    // println!("The length of '{}' is {}.", "Hello", len);
}
