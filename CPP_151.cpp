Here's the completed code:

long long double_the_difference(vector<float> lst) {
    long long sum = 0;
    for (float num : lst) {
        if (num > 0 && floor(num) == num) { // ignore negative numbers and non-integers
            if (static_cast<int>(num) % 2 != 0) { // check if the number is odd
                sum += pow(static_cast<int>(num), 2);
            }
        }
    }
    return sum;
}