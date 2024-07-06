Here's the completed code:

bool is_equal_to_sum_even(int n){
    for (int i = 2; ; i += 2) {
        int sum = 0;
        for (int j = i; sum < n && j <= 2 * i; j += 2) {
            sum += j;
        }
        if (sum == n)
            return true;
    }
}