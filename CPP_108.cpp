int count_nums(vector<int> nums) {
    int count = 0;
    for (auto num : nums) {
        if (num < 0)
            num = -num;
        bool has_positive_sum = false;
        while (num > 0) {
            int digit = num % 10;
            if (digit != 0 || num / 10 == 0)
                has_positive_sum = true;
            num /= 10;
        }
        if (has_positive_sum)
            count++;
    }
    return count;
}