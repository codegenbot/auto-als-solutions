Here is the completed code:

int search(vector<int> lst) {
    int max = 0;
    for (const auto &num : lst) {
        if (num > 0 && num >= max) {
            max = num;
        }
    }
    return max == 0 ? -1 : max;
}