bool will_it_fly(vector<int> q, int w) {
    vector<int> rev = q;
    reverse(rev.begin(), rev.end());
    if (q == rev) {  // balanced palindromic vector
        return accumulate(q.begin(), q.end(), 0) <= w;  // sum of elements less than or equal to maximum possible weight
    }
    return false;
}