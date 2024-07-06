int count_nums(vector<int> v) {
    int count = 0;
    for (int num : v) {
        if (num > 0) {
            int sign = abs(num) / pow(10, int(log10(abs(num)))) < 0 ? -1 : 1;
            int sum_digits = 0;
            while (abs(num)) {
                sum_digits += abs(num) % 10;
                num /= 10;
            }
            if (sign * sum_digits > 0)
                count++;
        } else if (num < 0) {
            num = -num;
            int sign = abs(num) / pow(10, int(log10(abs(num)))) < 0 ? -1 : 1;
            int sum_digits = 0;
            while (abs(num)) {
                sum_digits += abs(num) % 10;
                num /= 10;
            }
            if (sign * sum_digits > 0)
                count++;
        }
    }
    return count;
}