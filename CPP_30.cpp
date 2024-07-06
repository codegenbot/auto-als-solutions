#include <vector>
#include <cassert>

bool issame(const std::vector<float>& a, const std::vector<float>& b) {
    return a.size() == b.size() && std::equal(a.begin(), a.end(), b.begin());
}

vector<vector<float>> get_positive(vector<vector<float>> l) {
    vector<vector<float>> result;
    for (auto& nums : l) {
        vector<float> new_nums = get_positive(nums);
        if (!new_nums.empty()) {
            result.push_back(new_nums);
        }
    }
    return result;
}

int main() {
    vector<vector<float>> input = {{1.0, -2.0, 3.0}, {-4.0, 5.0, -6.0}};
    vector<vector<float>> output = get_positive(input);

    for (const auto& nums : output) {
        for (float num : nums) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}