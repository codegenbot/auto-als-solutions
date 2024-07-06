```
#include <vector>
#include <algorithm>

bool issame(vector<int> game, vector<int> guess) {
    if(game.size() != guess.size()) return false;
    for(int i = 0; i < game.size(); i++) {
        if(game[i] != guess[i]) return false;
    }
    return true;
}

vector<int> compare(vector<int> game, vector<int> guess) {
    if (!issame(game, guess)) {
        cout << "Invalid input. Guess must be the same size as the game." << endl;
        exit(1);
    }

    vector<int> result;
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i]) {
            result.push_back(0);
        } else {
            result.push_back(abs(guess[i] - game[i]));
        }
    }
    return result;
}