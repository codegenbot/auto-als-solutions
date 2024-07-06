```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

bool issame(const std::vector<int>& v1, const std::vector<int>& v2) {
    if (v1.size() != v2.size()) {
        return false;
    }
    for (int i = 0; i < v1.size(); ++i) {
        if (v1[i] != v2[i]) {
            return false;
        }
    }
    return true;
}

std::vector<int> common(std::vector<int> l1, std::vector<int> l2) {
    std::set<int> s1(l1.begin(), l1.end());
    std::set<int> s2(l2.begin(), l2.end());
    std::set<int> intersection;

    std::set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
        inserter(intersection, intersection.begin()));

    std::vector<int> result(intersection.begin(), intersection.end());
    return result;
}

int main() {
    std::vector<int> l1 = {1, 2, 3};
    std::vector<int> l2 = {2, 4, 5};

    if (issame(l1, l2)) {
        std::cout << "Vectors are same" << std::endl;
    } else {
        std::cout << "Vectors are not same" << std::endl;

        std::vector<int> common_elements = common(l1, l2);
        for (int i : common_elements) {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}