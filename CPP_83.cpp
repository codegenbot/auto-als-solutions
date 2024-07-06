int starts_one_ends(int n) {
    int count = 0;
    for (int i = 1; i <= 9; ++i) {
        if (i == 1 || i == 9) {
            count += pow(10, n - 1);
        } else {
            for (int j = 1; j < 10; ++j) {
                count++;
            }
        }
    }
    return count;
}