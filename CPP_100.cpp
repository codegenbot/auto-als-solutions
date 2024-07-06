#include <vector>
#include <algorithm>

bool issame(std::vector<int> a, std::vector<int> b) {
    return a.size() == b.size() && std::equal(a.begin(), a.end(), b.begin());
}

std::vector<int> make_a_pile(int n) {
    std::vector<int> pile;
    for (int i = 1; i <= n; i++)
        pile.push_back(i % 2 ? i * 2 - 1 : i * 2);
    return pile;
} 

int main() {
    assert(issame(make_a_pile(8), make_a_pile(8)) && "The test failed");
}