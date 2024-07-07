#include <iostream>
using namespace std;

int minOperations(vector<int> target, vector<vector<int>>& arr, int start) {
    int res = INT_MAX;
    for (int i = 0; i < arr.size(); i++) {
        int current_sum = 0;
        for (int j = 0; j < arr[i].size(); j++) {
            if (target[arr[i][j]] - 1 >= start) {
                current_sum++;
                target[arr[i][j]]--;
            }
        }
        res = min(res, current_sum);
    }
    return res;
}

int main() {
    vector<int> target = {5, 25, 15};
    vector<vector<int>> arr = {{2, 3, 8}, {1, 6, 18}};
    cout << "The minimum operations are: " << minOperations(target, arr, 0) << endl;
    return 0;
}