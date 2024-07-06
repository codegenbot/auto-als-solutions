#include <vector>

int count_nums(const vector<int>& n) {
    int count = 0;
    for (const auto& num : n) {
        if (num >= 0) {
            int sum = 0;
            bool has_negative = false;
            while (num > 0) {
                int digit = num % 10;
                if (digit < 0) {
                    has_negative = true;
                    break;
                }
                sum += digit;
                num /= 10;
            }
            if (!has_negative && sum > 0) {
                count++;
            }
        } else {
            int sum = 0;
            bool has_negative = false;
            while (num < 0) {
                int digit = -(-num % 10);
                if (digit < 0) {
                    has_negative = true;
                    break;
                }
                sum += digit;
                num -= digit * 10;
            }
            if (!has_negative && sum > 0) {
                count++;
            }
        }
    }
    return count;
}