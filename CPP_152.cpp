#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;

vector<int> compare(vector<int> game, vector<int> guess) {
    int cow = 0;
    int ox = 0;
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i]) {
            cow++;
        } else {
            if (guess[i] != i+1) {
                ox++;
            }
        }
    }
    vector<int> result;
    result.push_back(cow);
    result.push_back(ox);
    return result;
}