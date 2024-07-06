#include <iostream>
#include <vector>
using namespace std;

vector<int> compare(vector<int> scores, vector<int> guesses) {
    vector<int> differences;
    for (int i = 0; i < scores.size(); ++i) {
        int difference = abs(scores[i] - guesses[i]);
        differences.push_back(difference);
    }
    return differences;
}