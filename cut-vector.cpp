#include <vector>
using namespace std;

pair<vector<int>, vector<int>> cutVector(vector<int> vec) {
    int minDiff = INT_MAX;
    int index = -1;
    for (int i = 0; i < vec.size() - 1; i++) {
        int sum1 = 0, sum2 = 0;
        for (int j = 0; j <= i; j++) {
            sum1 += vec[j];
        }
        for (int j = i + 1; j < vec.size(); j++) {
            sum2 += vec[j];
        }
        int diff = abs(sum1 - sum2);
        if (diff < minDiff) {
            minDiff = diff;
            index = i;
        }
    }
    vector<int> left, right;
    for (int i = 0; i <= index; i++) {
        left.push_back(vec[i]);
    }
    for (int i = index + 1; i < vec.size(); i++) {
        right.push_back(vec[i]);
    }
    return {left, right};
}