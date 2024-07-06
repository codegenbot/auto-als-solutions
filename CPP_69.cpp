int search(vector<int> lst) {
    map<int, int> countMap;
    for (int num : lst) {
        if (countMap.find(num) == countMap.end()) {
            countMap[num] = 1;
        } else {
            countMap[num]++;
        }
    }

    int result = -1;
    for (auto it = countMap.begin(); it != countMap.end(); ++it) {
        if (it->second >= it->first && it->first > 0) {
            result = it->first;
            break;
        }
    }
    return result;
}