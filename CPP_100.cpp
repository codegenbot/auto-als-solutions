```cpp
#include <iostream>
#include <vector>
using namespace std;

bool isSame(vector<int> v1, vector<int> v2) {
    if(v1.size() != v2.size()) 
        return false;
    for(int i = 0; i < v1.size(); i++) {
        if(v1[i] != v2[i])
            return false;
    }
    return true;
}

vector<std::vector<int>> make_piles(int n) {
    vector<vector<int>> piles;
    for (int i = 0; i < n; i++) {
        vector<int> pile;
        int stones = 1;
        for (int j = 0; j <= i; j++) {
            if ((j + 1) % 2 == 0)
                stones += 2;
            else
                stones++;
            pile.push_back(stones);
        }
        piles.push_back(pile);
    }
    return piles;
}

int main() {
    int n;
    cout << "Enter the number of piles: ";
    cin >> n;
    vector<vector<int>> piles = make_piles(n);
    for (auto &pile : piles) {
        cout << "Pile: ";
        for (int stone : pile) {
            cout << stone << " ";
        }
        cout << endl;
    }

    return 0;
}