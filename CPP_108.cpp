int count_nums(vector<int> nums) {
    int count = 0;
    for (int num : nums) {
        bool has_nonzero_sum = false;
        int sign = (num < 0) ? -1 : 1;
        num = abs(num);
        while (num > 0) {
            int digit = num % 10;
            if (digit != 0 || sign == -1 && digit == 5)
                has_nonzero_sum = true;
            num /= 10;
        }
        if (has_nonzero_sum)
            count++;
    }
    return count;
}