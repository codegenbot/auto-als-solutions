```cpp
#include <vector>
#include <algorithm>

bool isSame(int a, int b) {
    return a == b;
}

bool areEqualVectors(std::vector<int> v1, std::vector<int> v2) {
    if (v1.size() != v2.size()) 
        return false;  
    for (int i = 0; i < v1.size(); i++) {
        if (!isSame(v1[i], v2[i])) 
            return false;
    } 
    return true;
}

std::vector<std::vector<int>> compare(std::vector<int> game, std::vector<int> guess) {
    std::vector<std::vector<int>> result(game.size());
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i]) {
            result[i] = {{0}};
        } else {
            result[i] = {{std::abs(game[i] - guess[i])}};
        }
    }
    return result;
}

int main_function() {
    std::vector<int> game = {1,2,3,5};
    std::vector<int> guess = {-1,2,3,4};
    assert(std::equal(compare(game,guess).begin(), compare(game,guess).end(), {{0},{0,{0}}}));
    return 0;
}