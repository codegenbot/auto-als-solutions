Here is the completed code:

int count_nums(vector<int> nums) {
    int count = 0;
    for (int num : nums) {
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
            } else if (has_negative) {
                int negative_sum = 0;
                while (num < 0) {
                    int digit = -(-num) % 10;
                    if (digit > 0) {
                        negative_sum += digit;
                    }
                    num /= 10;
                }
                if (negative_sum > 0) {
                    count++;
                }
            }
        }
    }
    return count;
}