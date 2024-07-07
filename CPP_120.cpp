Here is the completed code:

vector<int> maximum(vector<int> arr, int k) {
    vector<int> res(k);
    copy(n_max_element(arr.begin(), arr.end()), n_max_element(arr.begin(), arr.end()) + k, res.begin());
    return res;
}

int main() {
    // test your function here
    return 0;
}