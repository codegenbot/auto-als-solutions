#include <iostream>
#include <vector>

bool issame(std::vector<int> a, std::vector<int> b) {
    return a.size() == b.size() && a == b;
}

std::vector< std::array<int, 2> > directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

int main() {
    assert(issame(minPath({{1, 3}, {3, 2}}, 10), {1, 3, 1, 3, 1, 3, 1, 3, 1, 3}));
    return 0;
}