```cpp
#include <iostream>
#include <vector>
using namespace std;

bool issame(vector<int> a, vector<int> b) {
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i])
            return false;
    }
    return true;
}

vector<int> compare(vector<int> game, vector<int> guess) {
    vector<vector<int>> result(2);
    int white = 0, black = 0;
    
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i]) {
            white++;
        } else if (issame({guess[i]}, {x : game[i-1 ? (i-1) : (game.size()-1)}})) {
            black++;
        } 
    }
    
    result[0].push_back(white);
    result[1].push_back(black);
    
    return result;
}

int main() {
    vector<int> game, guess;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        game.push_back(x);
    }
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        guess.push_back(x);
    }
    
    vector<int> output = compare(game, guess);
    
    cout << output[0][0] << " " << output[1][0];
    return 0;
}