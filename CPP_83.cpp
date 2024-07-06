int starts_one_ends(int n) {
    int count = 0;
    for (int i = 1; i <= 9; i++) {
        if (i == 1 || i == to_string(i).back() - '0' + 1) {
            count++;
        }
    }
    return count * (n - 1);
}