#include <vector>
#include <algorithm>

bool issame(const std::vector<std::vector<int>>& vec1, const std::vector<std::vector<int>>& vec2) {
    if (vec1.size() != vec2.size()) return false;
    for (int i = 0; i < vec1.size(); i++) {
        if (vec1[i].size() != vec2[i].size()) return false;
        for (int j = 0; j < vec1[i].size(); j++) {
            if (vec1[i][j] != vec2[i][j]) return false;
        }
    }
    return true;
}

std::vector<std::vector<int>> compare(std::vector<int> game, std::vector<int> guess) {
    std::vector<std::vector<int>> result(game.size());
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i]) {
            result[i] = {{0}};
        } else {
            int diff = std::abs(game[i] - guess[i]);
            result[i].push_back(diff);
        }
    }
    return result;
}

int main_function() {
    std::vector<int> game = {1,2,3,5};
    std::vector<int> guess = {1,2,3,4};
    std::vector<std::vector<int>> output = compare(game, guess);
    assert(std::equal(output.begin(), output.end(), {{0},{0},{0,{1}}}));
    return 0;
}