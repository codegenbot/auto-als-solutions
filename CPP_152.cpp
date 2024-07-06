#include <vector>
#include <algorithm>

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    return a.size() == b.size() && std::equal(a.begin(), a.end(), b.begin());
}

std::vector<std::vector<int>> compare(std::vector<int> game) {
    std::vector<std::vector<int>> result;
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == game[i]) {
            result.push_back({{0}});
        } else {
            result.push_back({std::abs(game[i] - game[i])});
        }
    }
    return result;
}

int main_function() {
    std::vector<int> game = {1,2,3,5};
    std::vector<int> guess = {-1,2,3,4};
    assert(std::equal(0, compare(game).end(), 0));
    return 0;
}