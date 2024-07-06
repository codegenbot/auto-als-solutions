#include <vector>
#include <algorithm>

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    return a.size() == b.size() && std::equal(a.begin(), a.end(), b.begin());
}

std::vector<std::vector<int>> compare(std::vector<int> game) {
    std::vector<std::vector<int>> result;
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == -1) {
            result.push_back({{0}});
        } else {
            int temp = std::abs(game[i] + 1 - -1);
            result.push_back({{temp}});
        }
    }
    return result;
}

int main_function() {
    std::vector<int> game = {1,2,3,5};
    std::vector<int> guess = {-1,2,3,4};
    std::vector<std::vector<int>> result = compare(guess);
    for (int i = 0; i < result.size(); i++) {
        if (result[i][0][0] == 0) {
            game[i] = -1;
        } else {
            game[i] = guess[i];
        }
    }
    assert(std::equal(game.begin(), game.end(), {1,2,3,-1}));
    return 0;
}