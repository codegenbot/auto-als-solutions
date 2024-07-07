#include <vector>
#include <iostream>

int count_nums(std::vector<int> v) {
    int count = 0;
    for (int num : v) {
        bool has_positive_sum = false;
        if (num >= 0) {
            while (num > 0) {
                int digit = num % 10;
                if (digit != 0 || num / 10 == 0) {
                    has_positive_sum = true;
                    break;
                }
                num /= 10;
            }
        } else {
            while (num < 0) {
                int digit = -num % 10;
                if (digit != 0 && (-num) / 10 >= 0) {
                    has_positive_sum = true;
                    break;
                }
                num /= 10;
            }
        }
        if (!has_positive_sum) {
            count++;
        }
    }
    return count;
}

int main() {
    std::cout << count_nums({1, -2, 3, -4, 5, -6}) << std::endl;
    return 0;
}