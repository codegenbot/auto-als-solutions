int count_nums(vector<int> nums) {
    int count = 0;
    for (int num : nums) {
        bool has_positive_sum_of_digits = false;
        long abs_num = labs(num);
        while (abs_num > 0) {
            int digit = abs_num % 10;
            if (digit != 0 || sign(num) > 0) {
                has_positive_sum_of_digits = true;
                break;
            }
            abs_num /= 10;
        }
        if (has_positive_sum_of_digits) count++;
    }
    return count;
}

int sign(int n) {
    if (n > 0) return 1;
    else if (n < 0) return -1;
    else return 0;
}