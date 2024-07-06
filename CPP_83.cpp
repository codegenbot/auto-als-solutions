Here is the solution:

int starts_one_ends(int n) {
    int count = 0;
    for (long long i = 1; i <= (long long)pow(10, n-1); i++) {
        if ((i / pow(10, (n-1)/2)) % 10 == 1 || (i % pow(10, (n-1)/2)) % 10 == 1)
            count++;
    }
    return count;
}