```
long long double_the_difference(vector<float> lst) {
    long long sum = 0;
    for (float n : lst) {
        if (n > 0 && int(n) == n) { // check if number is positive and integer
            if (int(n) % 2 != 0) { // check if number is odd
                sum += pow(int(n), 2); // add square of the number to sum
            }
        }
    }
    return sum;
}