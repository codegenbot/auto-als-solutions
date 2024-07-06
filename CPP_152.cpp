#include <vector>
#include <algorithm>

bool issame(const std::vector<std::vector<int>>& v1, const std::vector<std::vector<int>>& v2) {
    if(v1.size()!=v2.size()) return false;
    for(size_t i=0; i<v1.size(); i++){
        if(v1[i].size()!=v2[i].size() || v1[i][0]!=v2[i][0]) return false;
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
    std::vector<int> guess = {1,2,3,5};
    assert(std::equal( compare(game,guess).begin(), compare(game,guess).end(), {{0},{0},{0,{0}}} ));
    return 0;
}