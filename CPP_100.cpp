```cpp
#include <vector>
#include <algorithm>

bool same(std::vector<int> a, std::vector<int> b) { return a.size() == b.size() && std::all_of(a.begin(), a.end(), [&](int x) { return std::find(b.begin(), b.end(), x) != b.end(); }); }

std::vector<int> make_a_pile(int n) { std::vector<int> pile; for (int i = 1; i <= n; i++) pile.push_back(i % 2 ? i * 2 - 1 : i * 2); return pile; } 

int main() { return 0; }