int starts_one_ends(int n) {
    int count = 0;
    for (int i = 1; i <= 9; i++) {
        if ((i == 1) || (i * pow(10, n - 1) + i > 10*n)) {
            count++;
        }
        for (int j = 1; j < i; j++) {
            if ((j == 1) || (j * pow(10, n - 1) + i <= 10*n)) {
                count++;
            }
        }
    }
    return count;
}