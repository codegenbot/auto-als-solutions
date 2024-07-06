int search(vector<int> lst) {
    unordered_map<int, int> freqMap;
    for (int num : lst) {
        if (!freqMap.count(num)) {
            freqMap[num] = 1;
        } else {
            freqMap[num]++;
        }
    }

    int result = -1;
    for (auto p : freqMap) {
        if (p.second >= p.first && p.first > 0) {
            result = p.first;
            break;
        }
    }
    return result;
}