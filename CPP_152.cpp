```cpp
#include <vector>
#include <algorithm>

bool issame(int a, int b) {
    return a == b;
}

std::vector<std::vector<int>> compare(std::vector<int> game, std::vector<int> guess) {
    std::vector<std::vector<int>> result(game.size());
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i]) {
            result[i] = {std::vector<int>{{0}}}; // modified here
        } else {
            result[i] = {{std::abs(game[i] - guess[i])}};
        }
    }
    return result;
}

int main_function() {
    std::vector<int> game = {1,2,3,5};
    std::vector<int> guess = {-1,2,3,4};
    assert(std::equal(compare(game,guess).begin(), compare(game,guess).end(), std::vector<int>{{0},{0},{0},{0}}));
    return 0;
}