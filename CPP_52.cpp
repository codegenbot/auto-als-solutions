```cpp
#include <iostream>
#include <vector>

bool below_threshold(std::vector<int> l, int t) {
    for (int i : l) {
        if (i >= t) {
            return false;
        }
    }
    return true;
}

int main() {
    std::vector<int> numbers;
    int threshold;

    // Read input from user
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;
    
    for (int i = 0; i < n; ++i) {
        int num;
        std::cout << "Enter element " << i + 1 << ": ";
        std::cin >> num;
        numbers.push_back(num);
    }

    std::cout << "Enter the threshold: ";
    std::cin >> threshold;

    // Call function and print result
    if (below_threshold(numbers, threshold)) {
        std::cout << "All elements are below the threshold." << std::endl;
    } else {
        std::cout << "Not all elements are below the threshold." << std::endl;
    }

    return 0;
}