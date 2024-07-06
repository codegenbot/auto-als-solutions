#include <vector>
#include <algorithm>

bool same(std::vector<int> a, std::vector<int> b) {
    return a.size() == b.size() && std::all_of(a.begin(), a.end(), [&](int x) { return std::find(b.begin(), b.end(), x) != b.end(); });
}

std::vector<int> make_a_pile(int n) {
    std::vector<int> pile;
    for (int i = 1; i <= n; i++)
        pile.push_back(i % 2 ? i * 2 - 1 : i * 2);
    return pile;
} 

bool checkPiles(std::vector<int> a, std::vector<int> b) {
    return same(a, b);
}

int main() {
    bool result = checkPiles(make_a_pile(8), make_a_pile(16));
    if (!result) {
        std::cout << "Piles are not the same." << std::endl;
    } else {
        std::cout << "Piles are the same." << std::endl;
    }
}