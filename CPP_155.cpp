vector<int> even_odd_count(int num) {
    int ev = 0, od = 0;
    string str = to_string(abs(num));
    for (char c : str) {
        if (c - '0' % 2 == 0) ev++;
        else od++;
    }
    return {ev, od};
}