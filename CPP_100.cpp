#include <vector>

bool issame(std::vector<int> a, std::vector<int> b) {
    return a == b;
}

std::vector<int> make_a_pile(int n) {
    vector<int> pile;
    int stones = 1;
    for (int i = 0; i < n; i++) {
        if ((i + 1) % 2 == 0)
            stones += 2;
        else
            stones++;
        pile.push_back(stones);
    }
    return pile;
}