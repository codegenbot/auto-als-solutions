int smallest_change(vector<int> arr) {
    int n = arr.size();
    string str = "";
    for (int i : arr) {
        str += to_string(i);
    }
    string rev_str = str;
    reverse(rev_str.begin(), rev_str.end());
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (str[i] != rev_str[i]) {
            count++;
        }
    }
    return count;
}