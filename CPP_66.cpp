Here is the completed code:

```
int digitSum(string s) {
    int sum = 0;
    for (char c : s) {
        if (isupper(c)) {
            sum += (int)c;
        }
    }
    return sum;
}