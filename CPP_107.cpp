vector<int> even_odd_palindrome(int n) {
    vector<int> result(2);
    int even = 0;
    int odd = 0;

    for (int i = 1; i <= n; ++i) {
        string str = to_string(i);
        bool isPalindrome = true;
        int left = 0, right = str.length() - 1;

        while (left < right) {
            if (str[left] != str[right]) {
                isPalindrome = false;
                break;
            }
            left++;
            right--;
        }

        if (isPalindrome && i % 2 == 0)
            even++;
        else if (isPalindrome && i % 2 != 0)
            odd++;

    }
    result[0] = even;
    result[1] = odd;

    return result;
}