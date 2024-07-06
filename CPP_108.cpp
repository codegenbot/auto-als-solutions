int count_nums(vector<int> nums) {
    int count = 0;
    for (int num : nums) {
        bool has_positive_sum_of_digits = false;
        if (num >= 0) {
            int sum = 0;
            while (num > 0) {
                int digit = num % 10;
                sum += abs(digit);
                num /= 10;
            }
            if (sum > 0) has_positive_sum_of_digits = true;
        } else {
            num = -num;
            int sum = 0, first_non_zero_digit_index = -1;
            for (int i = 0; num > 0; ++i) {
                int digit = num % 10;
                if (digit != 0) first_non_zero_digit_index = i;
                num /= 10;
                sum += abs(digit);
            }
            if (sum > 0 && first_non_zero_digit_index >= 0)
                has_positive_sum_of_digits = true;
        }
        if (has_positive_sum_of_digits) count++;
    }
    return count;
}