#include <initializer_list>
#include <vector>

bool std::operator==(const std::vector<int>& a, const std::vector<int>& b) {
    return a.size() == b.size() && std::all_of(a.begin(), a.end(), [&](int x) { return std::find(b.begin(), b.end(), x) != b.end(); });
}

std::vector<int> compare(std::vector<int> game, std::vector<int> guess) {
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

int main_function() {
    assert(std::issame(compare({1,2,3,5},{-1,2,3,4}),{2,0,0,1}));
    return 0;
}