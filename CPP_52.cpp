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
    std::vector<int> list;
    int threshold;

    // Read input from user
    std::cout << "Enter the elements of the list: ";
    for (int i = 0; i < 5; ++i) {
        int num;
        std::cin >> num;
        list.push_back(num);
    }

    std::cout << "Enter the threshold value: ";
    std::cin >> threshold;

    // Check if all elements in the list are below the threshold
    bool result = below_threshold(list, threshold);

    // Print the output
    if (result) {
        std::cout << "All elements in the list are below the threshold." << std::endl;
    } else {
        std::cout << "At least one element in the list is not below the threshold." << std::endl;
    }

    return 0;
}