```cpp
#include <iostream>
#include <vector>

using namespace std;

bool issame(const vector<vector<int>>& vec1, const vector<vector<int>>& vec2) {
    if (vec1.size() != vec2.size()) return false;
    for (int i = 0; i < vec1.size(); i++) {
        if (vec1[i].size() != vec2[i].size()) return false;
        for (int j = 0; j < vec1[i].size(); j++) {
            if (vec1[i][j] != vec2[i][j]) return false;
        }
    }
    return true;
}

vector<vector<int>> compare(vector<int> game, vector<int> guess) {
    vector<vector<int>> result(game.size());
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i]) {
            result[i] = {{0}};
        } else {
            result[i] = {{abs(game[i] - guess[i])}};
        }
    }
    return result;
}

int main_function() {
    vector<int> game = {0, 1, 2, 4};
    vector<int> guess = {-1, 2, 3, 4};
    assert(issame(compare(game,guess), {{0},{0},{0,{0}}})); 
    return 0;
}