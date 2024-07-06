```cpp
#include <iostream>
#include <vector>

bool below_threshold(std::vector<int> l, int t) {
    for (int num : l) {
        if (num >= t) {
            return false;
        }
    }
    return true;
}

int main() {
    std::vector<int> list = {1, 2, 3};
    int threshold = 3;
    bool result = below_threshold(list, threshold);
    
    if(result) {
        std::cout << "All elements in the list are below the threshold." << std::endl;
    } else {
        std::cout << "At least one element in the list is not below the threshold." << std::endl;
    }
    
    return 0;
}