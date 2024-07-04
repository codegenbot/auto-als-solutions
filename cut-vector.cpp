#include <vector>
#include <iostream>
#include <cmath>
#include <climits>
using namespace std;

int main() {
    vector<int> nums;
    int num;
    while (cin >> num) {
        nums.push_back(num);
    }

    int total_sum = 0;
    for (int n : nums) total_sum += n;

    int left_sum = 0, min_diff = INT_MAX, cut_index = 0;
    for (int i = 0; i < nums.size(); ++i) {
        left_sum += nums[i];
        int right_sum = total_sum - left_sum;
        int diff = abs(left_sum - right_sum);
        if (diff < min_diff) {
            min_diff = diff;
            cut_index = i + 1;
        }
    }

    for (int i = 0; i < cut_index; ++i) {
        cout << nums[i] << " ";
    }
    cout << endl;
    for (int i = cut_index; i < nums.size(); ++i) {
        cout << nums[i] << " ";
    }
    cout << endl;

    return 0;
}