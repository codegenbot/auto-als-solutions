#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;

vector<int> compare(vector<int> scores, vector<int> guesses) {
    vector<int> results;
    for (int i = 0; i < scores.size(); i++) {
        int diff = abs(scores[i] - guesses[i]);
        if (scores[i] == guesses[i]) {
            results.push_back(0);
        } else {
            results.push_back(diff);
        }
    }
    return results;
}