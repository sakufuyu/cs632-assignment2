#include <iostream>
#include <vector>
#include <memory>

std::vector<int>* createLargeArray() {
    std::cout << "Creating large array" << std::endl;
    // Allocate a vector with 1 million integers (~4MB)
    std::vector<int>* data = new std::vector<int>();
    data->reserve(1000000);
    std::cout << "Array created with capacity: " << data->capacity() << std::endl;
    return data;
}

void processData(const std::vector<int>* data) {
    std::cout << "Processing data (pointer) of capacity: " << data->capacity() << std::endl;
    // In C++, we're working with a pointer which must be managed
}

int main() {
    std::cout << "C++ memory management demo" << std::endl;
    
    {
        // Create data - manually managed
        std::vector<int>* largeData = createLargeArray();
        
        // Pass the pointer
        processData(largeData);
        
        std::cout << "End of inner scope - must manually delete largeData" << std::endl;
        
        // Manual memory management requires explicit deallocation
        delete largeData;
    } // largeData pointer goes out of scope, but memory would leak without delete
    
    std::cout << "Memory has been manually freed" << std::endl;
    
    return 0;
}