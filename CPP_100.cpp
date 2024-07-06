#include <vector>
#include <algorithm>

bool isSamePile(std::vector<int> a, std::vector<int> b) { return a.size() == b.size() && std::all_of(a.begin(), a.end(), [&](int x) { return std::find(b.begin(), b.end(), x) != b.end(); }); }

std::vector<int> make_a_pile(int n) { std::vector<int> pile; for (int i = 1; i <= n; i++) pile.push_back(i % 2 ? i * 2 - 1 : i * 2); return pile; } 

int main() {
    assert(isSamePile(make_a_pile(8), {3,5,7,9,11,13,15,17}));
    return 0;
}