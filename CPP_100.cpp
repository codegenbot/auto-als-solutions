#include <vector>
#include <cassert>

std::vector<int> make_a_pile(int n) {
    std::vector<int> pile;
    for (int i = 8; i <= 22 + (n - 1) * 2; i += 2) {
        pile.push_back(i);
    }
    return pile;
}

bool issame(std::vector<int> a, std::vector<int> b) { return a == b; }

int main() {
    int x;
    std::vector<int> pile = make_a_pile(8);
    assert(issame(pile, {8, 10, 12, 14, 16, 18, 20, 22}));
}