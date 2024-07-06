#include <vector>
#include <cassert>

std::vector<int> generate_integers(int min, int max) {
    std::vector<int> integers;
    for (int i = min; i <= max; i++) {
        integers.push_back(i);
    }
    return integers;
}

int main_test() {
    std::vector<int> a = generate_integers(17, 89);
    assert(std::equal(a.begin(), a.end(), a.begin()));
    return 0;
}