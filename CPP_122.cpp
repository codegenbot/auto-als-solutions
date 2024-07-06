#include <vector>
#include <algorithm>

int add_elements(std::vector<int> arr, int k) {
    std::vector<int> two_digit_nums;
    for (int i = 0; i < k; i++) {
        if (std::to_string(arr[i]).size() <= 2) {
            two_digit_nums.push_back(arr[i]);
        }
    }
    int sum = 0;
    for (int num : two_digit_nums) {
        sum += num;
    }
    return sum;
}