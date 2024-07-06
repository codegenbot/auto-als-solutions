#include <initializer_list>
#include <vector>

int count_nums(std::vector<int> nums) {
    int count = 0;
    for (int num : nums) {
        bool has_positive_sum = false;
        if (num < 0) {
            num = -num;
        }
        while (num > 0) {
            int digit = num % 10;
            if (digit != 0) {
                has_positive_sum = true;
                break;
            }
            num /= 10;
        }
        if (has_positive_sum) {
            count++;
        }
    }
    return count;

std::size_t _M_len;
constexpr std::size_t size() const { return _M_len; }