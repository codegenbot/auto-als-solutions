#include <vector>
#include <algorithm>

std::vector<int> generate_integers(int a, int b) {
    std::vector<int> integers;
    for (int i = a; i <= b; i++) {
        integers.push_back(i);
    }
    return integers;
}

bool issame(std::vector<int> a, std::vector<int> b) {
    return a == b;
}

int main_test() {
    assert(generate_integers(17, 89) == generate_integers(17, 89));
    return 0;
}