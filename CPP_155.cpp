vector<int> even_odd_count(int num) {
    int countEven = 0;
    int countOdd = 0;

    if (num < 0)
        num = -num;

    while (num > 0) {
        int digit = num % 10;
        if (digit % 2 == 0)
            countEven++;
        else
            countOdd++;
        num /= 10;
    }

    vector<int> result;
    result.push_back(countEven);
    result.push_back(countOdd);

    return result;
}