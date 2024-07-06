Here is the solution:

vector<int> even_odd_count(int num) {
    int countEven = 0, countOdd = 0;
    while (num != 0) {
        int digit = num % 10;
        if (digit % 2 == 0)
            countEven++;
        else
            countOdd++;
        num /= 10;
    }
    return {countEven, countOdd};
}