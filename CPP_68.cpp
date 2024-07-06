#include <vector>
#include <algorithm>

bool const &issame(std::vector<int>& a, std::vector<int>& b) {
    return a == b;
}

int main() {
    assert(issame(pluck({7, 9, 7, 1}), {})); 
    return 0;
}