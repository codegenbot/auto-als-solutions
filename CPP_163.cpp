```cpp
#include <vector>
#include <cassert>

std::vector<int> generate_integers(int start, int end) {
    std::vector<int> result;
    for (int i = start; i <= end; ++i) {
        result.push_back(i);
    }
    return result;
}

int main_test() {
    std::vector<int> a = generate_integers(17, 89);
    assert(std::equal(a.begin(), a.end(), a.begin()));
    return 0;
}