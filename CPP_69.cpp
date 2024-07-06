int search(vector<int> lst) {
    map<int, int> freq;
    for (int i : lst) {
        if (freq.find(i) == freq.end()) {
            freq[i] = 1;
        } else {
            freq[i]++;
        }
    }

    int max_freq = -1;
    for (auto p : freq) {
        if (p.second > max_freq) {
            max_freq = p.second;
        }
    }

    return max_freq;
}