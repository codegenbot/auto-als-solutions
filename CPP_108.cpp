int count_nums(vector<int> nums) {
    int count = 0;
    for (int num : nums) {
        if (num < 0) {
            num = -num;
        }
        bool has_nonzero_sum = false;
        while (num > 0) {
            int digit = num % 10;
            if (digit != 0 || (num / 10 == 0 && digit == -1)) {
                has_nonzero_sum = true;
                break;
            }
            num /= 10;
        }
        if (has_nonzero_sum) {
            count++;
        }
    }
    return count;
}