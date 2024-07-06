```
#include <vector>

bool same(vector<int> a, vector<int> b) { return a.size() == b.size() && all_of(a.begin(), a.end(), [b](int x) { return find(b.begin(), b.end(), x) != b.end(); }); }

vector<int> make_a_pile(int n) { vector<int> pile; for (int i = 1; i <= n; i++) pile.push_back(i % 2 ? i * 2 - 1 : i * 2); return pile; } 

void main() { assert(same(make_a_pile(8), {1, 2, 4, 6, 8, 10, 12, 14})); }