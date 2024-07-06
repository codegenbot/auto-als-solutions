```cpp
#include <vector>
#include <iostream>

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
    std::cout << "Enter the number of elements: ";
    int n; std::cin >> n;
    for (int i = 0; i < n; ++i) {
        std::cout << "Enter element " << i + 1 << ": ";
        int num; std::cin >> num;
        numbers.push_back(num);
    }
    std::cout << "Enter the threshold: ";
    std::cin >> threshold;

    // Print output
    if (below_threshold(numbers, threshold)) {
        std::cout << "All elements are below the threshold.\n";
    } else {
        std::cout << "Not all elements are below the threshold.\n";
    }

    return 0;
}