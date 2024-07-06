#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> l;
    int num;
    
    // Read input from user
    while (true) {
        std::cin >> num;
        
        if (num == -1)
            break;
            
        l.push_back(num);
    }
    
    // Find the maximum element in the vector
    return *std::max_element(l.begin(), l.end());
}