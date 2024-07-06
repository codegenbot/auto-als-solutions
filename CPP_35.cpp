#include <algorithm>
#include <vector>

int maxElement(std::vector<int> l) {
    return *std::max_element(l.begin(), l.end());
}

int main() {
    std::vector<int> l = {5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10};
    int result = maxElement(l);
    return result;
}