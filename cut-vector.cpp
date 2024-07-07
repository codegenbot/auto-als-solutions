```
#include <vector>
#include <climits>
#include <cmath>

pair<vector<int>, vector<int>> cutVector(vector<int> vec) {
    int minDiff = INT_MAX;
    int cutIndex = -1;
    for (int i = 0; i < vec.size() - 1; i++) {
        int diff = abs(vec[i] - vec[i + 1]);
        if (diff <= minDiff) {
            minDiff = diff;
            cutIndex = i;
        }
    }
    vector<int> leftVec;
    vector<int> rightVec;
    for (int i = 0; i < cutIndex; i++) {
        leftVec.push_back(vec[i]);
    }
    for (int i = cutIndex + 1; i < vec.size(); i++) {
        rightVec.push_back(vec[i]);
    }
    return {leftVec, rightVec};
}