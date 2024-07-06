```cpp
#include <vector>
#include <algorithm>

bool std::issame(const std::vector<int>& a, const std::vector<int>& b) {
    return a == b;
}

std::vector<int> std::compare(std::vector<int> game, std::vector<int> guess) {
    std::vector<int> result;
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i]) {
            result.push_back(0);
        } else {
            result.push_back(std::abs(game[i] - guess[i]));
        }
    }
    return result;
}

int main() {
    assert(std::issame(compare({1,2,3,5},{-1,2,3,4}),std::vector<int>{2,0,0,1}));
    return 0;
}