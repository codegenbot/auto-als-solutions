#include <vector>

bool issame(const std::vector<std::vector<int>>& a, const std::vector<std::vector<int>>& b) {
    return std::equal(a.begin(), a.end(), b.begin());
}

std::vector<std::vector<int>> compare(const std::vector<int>& game, const std::vector<int>& guess) {
    std::vector<std::vector<int>> result;
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i]) {
            result.push_back({{0}});
        } else {
            if(std::abs(game[i]-guess[i])<1){
                result.push_back({{0,1}}); // correct values in the inner vector
            }
            else{
                result.push_back({{std::abs(game[i] - guess[i])}});
            }
        }
    }
    return result;
}

int main_function() {
    std::vector<int> game = {1,2,3,5};
    std::vector<int> guess = {-1,2,3,4};
    assert(std::issame(compare(game,guess),{{0},{0},{0,{1}}}));
    return 0;
}