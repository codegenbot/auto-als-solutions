Here is the completed code:

int search(vector<int> lst) {
    unordered_map<int, int> freq;
    for (int num : lst) {
        if (freq.find(num) == freq.end()) {
            freq[num] = 1;
        } else {
            freq[num]++;
        }
    }
    for (auto& pair : freq) {
        if (pair.second >= pair.first && pair.first > 0) {
            return pair.first;
        }
    }
    return -1;
}