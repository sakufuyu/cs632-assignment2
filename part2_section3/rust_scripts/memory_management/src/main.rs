fn create_large_array() -> Vec<i32> {
    println!("Creating large array");
    // Allocate a vector with 1 million integers (~4MB)
    let data = Vec::with_capacity(1_000_000);
    println!("Array created with capacity: {}", data.capacity());
    data
}

fn process_data(data: &Vec<i32>) {
    println!("Processing data (borrowed) of capacity: {}", data.capacity());
    // Demonstrate borrowing - data is not owned here
}

fn main() {
    // Memory is automatically managed through ownership
    println!("Rust memory management demo");
    
    {
        // Create data - ownership is given to this scope
        let large_data = create_large_array();
        
        // Pass a reference (borrowing) 
        process_data(&large_data);
        
        println!("End of inner scope - large_data will be dropped");
    } // large_data goes out of scope and is automatically freed here
    
    // Trying to use large_data here would be a compile-time error
    println!("Memory has been automatically freed");
}