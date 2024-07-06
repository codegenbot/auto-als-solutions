```cpp
namespace std;

bool issame(vector<int> a, vector<int> b) {
    return a.size() == b.size() && equal(a.begin(), a.end(), b.begin());
}

vector<vector<int>> compare(vector<int> game, vector<int> guess) {
    vector<vector<int>> result;
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i]) {
            result.push_back({{0}});
        } else {
            vector<int> temp = {std::abs(game[i] - guess[i])};
            result.push_back(temp);
        }
    }
    return result;
}

int main_function() {
    vector<int> game = {1,2,3,5};
    vector<int> guess = {-1,2,3,4};
    assert(std::issame(compare(game,guess), {{0},{0,{0}}}));
    return 0;
}