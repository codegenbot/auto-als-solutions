bool will_it_fly(vector<int> q, int w) {
    string s = "";
    for (int i : q) {
        s += to_string(i);
    }
    if (!s.compare(to_string(s))) {
        return accumulate(q.begin(), q.end(), 0) <= w;
    } else {
        return false;
    }
}