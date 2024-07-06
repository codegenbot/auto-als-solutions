#include <vector>
#include <algorithm>

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    return a == b;
}

std::vector<int> compare(std::vector<int> game, std::vector<int> guess) {
    std::vector<int> result;
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i]) {
            result.push_back(0);
        } 
        else {
            if ((game[i] > guess[i]) && (guess[i]%2) == 0) {
                result.push_back(1);
            }
            else if ((game[i] < guess[i]) && (game[i]%2) != 0) {
                result.push_back(-1);
            } 
            else {
                if (game[i]%2 == 0)
                    result.push_back(1);
                else
                    result.push_back(-1);
            }
        }
    }
    return result;
}

int main_function() {
    assert(std::issame(compare({1,2,3,5},{-1,2,3,4}),{2,0,0,1}));
    return 0;
}