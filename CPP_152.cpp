#include <vector>
#include <algorithm>

bool issame(std::vector<int> a, std::vector<int> b) {
    return a == b;
}

std::vector<std::vector<int>> compare(std::vector<int> game, std::vector<int> guess) {
    std::vector<std::vector<int>> result;
    
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i]) {
            result.push_back({{1}}); // Correct
        } else if (std::abs(game[i]-guess[i]) <= 1) {
            result.push_back({{2}});
        } else {
            result.push_back({{0}});
        }
    }
    return result;
}

int main_function() {
    std::vector<int> game = {1,2,3,5};
    std::vector<int> guess = {-1,2,3,4};
    
    auto actual = compare(game,guess);
    auto expected = {{1}, {2, 0}, {2, 0}, {0}};
    for (int i = 0; i < 4; ++i)
        assert(std::equal(actual[i].begin(), actual[i].end(), expected[i].begin()));
    
    return 0;
}