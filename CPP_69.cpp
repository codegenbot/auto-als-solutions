int search(vector<int> lst) {
    map<int, int> freq;
    for (int i : lst) {
        if (freq.find(i) == freq.end()) {
            freq[i] = 1;
        } else {
            freq[i]++;
        }
    }

    int max_freq_key = -1;
    for (auto p : freq) {
        if (p.second > max_freq_key && p.second >= p.first && p.first > 0) {
            max_freq_key = p.second;
        }
    }

    return max_freq_key;
}