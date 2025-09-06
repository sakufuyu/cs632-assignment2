import java.util.ArrayList;

public class MemoryManagement {
    
    private static ArrayList<Integer> createLargeArray() {
        System.out.println("Creating large array");
        // Allocate array list with initial capacity for 1 million integers
        ArrayList<Integer> data = new ArrayList<>(1_000_000);
        System.out.println("Array created with capacity: " + data.size());
        return data;
    }
    
    private static void processData(ArrayList<Integer> data) {
        System.out.println("Processing data (reference) of capacity: " + data.size());
        // In Java, references are passed but garbage collection handles memory
    }
    
    public static void main(String[] args) {
        System.out.println("Java memory management demo");
        
        {
            // Create data - managed by garbage collector
            ArrayList<Integer> largeData = createLargeArray();
            
            // Pass the reference
            processData(largeData);
            
            System.out.println("End of inner block - reference will go out of scope");
        } // largeData reference goes out of scope, but memory not immediately freed
        
        System.out.println("Memory will be freed by garbage collector when needed");
        
        // Trigger garbage collection (just for demonstration)
        System.gc();
    }
}