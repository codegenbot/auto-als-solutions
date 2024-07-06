#include <vector>
#include <algorithm>

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    return a.size() == b.size() && std::equal(a.begin(), a.end(), b.begin());
}

std::vector<std::pair<int, int>> compare(std::vector<int> game, std::vector<int> guess) {
    std::vector<std::pair<int, int>> result;
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i]) {
            result.push_back({{i, 0}});
        } else {
            result.push_back({{i, std::abs(game[i] - guess[i])}});
        }
    }
    return result;
}

int main_function() {
    std::vector<int> game = {1,2,3,5};
    std::vector<int> guess = {-1,2,3,4};
    assert(std::equal(compare(game,guess).begin(), compare(game,guess).end(), {{0,0}}));
    return 0;
}