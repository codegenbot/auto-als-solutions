```cpp
#include <vector>

bool issame(vector<int> a,vector<int>b){
    if(a.size() != b.size())
        return false;
    for(int i=0;i<a.size();i++){
        if(a[i] != b[i])
            return false;
    }
    return true;
}

vector<int> make_a_pile(int n) {
    vector<int> pile;
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0)
            pile.push_back(i * 2 - 1);
        else
            pile.push_back(i * 2);
    }
    return pile;
}

bool check(int n) {
    vector<int> pile = make_a_pile(n);
    vector<int> correctPile = {1, 2, 4, 6, 8, 10, 12, 14};
    if (!issame(pile, correctPile)) {
        return false;
    }
    return true;
}

int main() {
    assert(check(8));
    return 0;
}