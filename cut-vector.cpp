#include <vector>
using namespace std;

vector<vector<int>> cutVector(vector<int> vec) {
    int n = vec.size();
    vector<vector<int>> res(2);
    for (int i = 0; i < n; i++) {
        if (i == 0 || i == n - 1) {
            res[0].push_back(vec[i]);
            res[1].push_back(vec[i]);
        } else {
            int left_sum = 0, right_sum = 0;
            for (int j = 0; j < i; j++) {
                left_sum += vec[j];
            }
            for (int j = i; j < n; j++) {
                right_sum += vec[j];
            }
            if (left_sum == right_sum) {
                res[0].push_back(vec[i]);
                res[1].push_back(vec[i]);
            } else {
                int min_diff = abs(left_sum - right_sum);
                for (int j = 0; j < i; j++) {
                    left_sum -= vec[j];
                    if (abs(left_sum - right_sum) < min_diff) {
                        res[0].clear();
                        res[1].clear();
                        res[0].push_back(vec[j]);
                        res[1].push_back(vec[i]);
                        for (int k = 0; k < j; k++) {
                            res[0].push_back(vec[k]);
                        }
                        for (int k = i + 1; k < n; k++) {
                            res[1].push_back(vec[k]);
                        }
                        min_diff = abs(left_sum - right_sum);
                    }
                }
                for (int j = i; j < n; j++) {
                    right_sum -= vec[j];
                    if (abs(left_sum - right_sum) < min_diff) {
                        res[0].clear();
                        res[1].clear();
                        res[0].push_back(vec[i]);
                        res[1].push_back(vec[j]);
                        for (int k = 0; k < i; k++) {
                            res[0].push_back(vec[k]);
                        }
                        for (int k = j + 1; k < n; k++) {
                            res[1].push_back(vec[k]);
                        }
                        min_diff = abs(left_sum - right_sum);
                    }
                }
            }
        }
    }
    return res;
}