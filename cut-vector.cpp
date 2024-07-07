#include <vector>
#include <iostream>

std::vector<int> cutVector(const std::vector<int>& nums) {
    int minDiff = INT_MAX;
    int cutIndex = 0;

    for (int i = 1; i < nums.size(); ++i) {
        int diff = nums[i] - nums[0];
        if (diff <= minDiff) {
            minDiff = diff;
            cutIndex = i;
        }
    }

    return {std::vector<int>(nums.begin(), nums.begin() + cutIndex),
            std::vector<int>(nums.begin() + cutIndex, nums.end())};
}

int main() {
    int n;
    std::cin >> n;

    std::vector<int> nums(n);
    for (auto& num : nums) {
        std::cin >> num;
    }

    auto res = cutVector(nums);

    std::cout << res[0].size() << '\n';
    for (int num : res[0]) {
        std::cout << num << ' ';
    }
    std::cout << '\n';

    std::cout << res[1].size() << '\n';
    for (int num : res[1]) {
        std::cout << num << ' ';
    }
    std::cout << '\n';

    return 0;
}