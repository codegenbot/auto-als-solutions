vector<int> even_odd_count(int num) {
    vector<int> result(2);
    int abs_num = abs(num);

    while (abs_num > 0) {
        int digit = abs_num % 10;
        if (digit % 2 == 0)
            result[0]++;
        else
            result[1]++;
        abs_num /= 10;
    }
    return result;
}