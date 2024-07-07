#include <vector>
#include <iostream>

int count_nums(std::vector<int> v) {
    int count = 0;
    for (int num : v) {
        bool has_positive_sum = false;
        if (num < 0) {
            num = -num;
        }
        while (num > 0) {
            int digit = num % 10;
            if (digit != 0 || num / 10 == 0) {
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
}

int main() {
    assert(count_nums({1}) == 1);
    return 0;
}