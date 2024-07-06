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
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;

    std::vector<int> v;
    for(int i = 0; i < n; ++i) {
        int x;
        std::cout << "Enter element " << i+1 << ": ";
        std::cin >> x;
        v.push_back(x);
    }

    int threshold;
    std::cout << "Enter the threshold: ";
    std::cin >> threshold;

    if(below_threshold(v, threshold)) {
        std::cout << "All elements are below the threshold." << std::endl;
    } else {
        std::cout << "At least one element is not below the threshold." << std::endl;
    }

    return 0;
}