#include <vector>
#include <algorithm>

bool issame(std::vector<int> a, std::vector<int> b) {
    return a == b;
}

std::vector<int> strange_sort_list(std::vector<int> lst) {
    std::vector<int> result;
    while (!lst.empty()) {
        int min_val = *min_element(lst.begin(), lst.end());
        result.push_back(min_val);
        lst.erase(remove(lst.begin(), lst.end(), min_val), lst.end());
        
        if (!lst.empty()) {
            int max_val = *max_element(lst.begin(), lst.end());
            lst.erase(remove(lst.begin(), lst.end(), max_val), lst.end());
        } else {
            result.push_back(*min_element(lst.begin(), lst.end()));
        }
    }
    return result;
}

int main() {
    std::vector<int> testVector{5, 3, 8, 4, 2};
    std::cout << "Original Vector: ";
    for (int num : testVector) {
        std::cout << num << " ";
    } std::cout << "\n";
    std::vector<int> sortedVector = strange_sort_list(testVector);
    std::cout << "Sorted Vector: ";
    for (int num : sortedVector) {
        std::cout << num << " ";
    }
    return 0;
}