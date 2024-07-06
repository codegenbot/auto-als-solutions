#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int findMaximumSum(vector<vector<int>>& v) {
    int max_sum = 0;
    for (const auto& row : v) {
        int current_sum = 0;
        for (int num : row) {
            current_sum += abs(num);
        }
        if (current_sum > max_sum)
            max_sum = current_sum;
    }
    return max_sum;
}