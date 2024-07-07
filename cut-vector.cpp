#include <vector>
using namespace std;

vector<vector<int>> cutVector(vector<int>& v) {
    int min_diff = INT_MAX;
    int split_idx = -1;

    for (int i = 0; i < v.size() - 1; i++) {
        int left_sum = 0, right_sum = 0;
        for (int j = 0; j <= i; j++) {
            left_sum += v[j];
        }
        for (int k = i + 1; k < v.size(); k++) {
            right_sum += v[k];
        }

        int diff = abs(left_sum - right_sum);
        if (diff < min_diff) {
            min_diff = diff;
            split_idx = i;
        }
    }

    vector<vector<int>> result(2);
    for (int i = 0; i <= split_idx; i++) {
        result[0].push_back(v[i]);
    }
    for (int i = split_idx + 1; i < v.size(); i++) {
        result[1].push_back(v[i]);
    }

    return result;
}