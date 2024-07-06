#include <initializer_list>
#include <vector>

int count_nums(std::vector<int> nums) {
    int count = 0;
    std::size_t _M_len;
    constexpr std::size_t size() const { return _M_len; }
    for (std::size_t i = 0; i < size(); ++i) {
        bool has_positive_sum = false;
        if (nums[i] < 0) {
            nums[i] = -nums[i];
        }
        while (nums[i] > 0) {
            int digit = nums[i] % 10;
            if (digit != 0) {
                has_positive_sum = true;
                break;
            }
            nums[i] /= 10;
        }
        if (has_positive_sum) {
            count++;
        }
    }
    return count;