```
#include <iostream>
#include <vector>
using namespace std;

bool issame(int a, int b) {
    if (a == b)
        return true;
    else
        return false;
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

int main() {
    int n;
    cout << "Enter the number of piles: ";
    cin >> n;
    std::vector<int> pile = make_a_pile(n);

    for (auto i : pile) {
        if (issame(i, 1))
            cout << "The " << (pile.size() - i + 1) << "th pile has one stone.\n";
        else
            cout << "The " << (pile.size() - i + 1) << "th pile has " << i << " stones.\n";
    }

    return 0;
}