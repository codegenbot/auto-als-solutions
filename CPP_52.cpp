```cpp
#include <vector>
#include <algorithm>

bool below_threshold(std::vector<int> l, int t) {
    for (int num : l) {
        if (num >= t) {
            return false;
        }
    }
    return true;
}

int main() {
    std::vector<int> numbers = {1, 2, 3, 4};
    int threshold = 3;
    if (below_threshold(numbers, threshold)) {
        std::cout << "All elements are below the threshold." << std::endl;
    } else {
        std::cout << "At least one element is not below the threshold." << std::endl;
    }
    return 0;
}