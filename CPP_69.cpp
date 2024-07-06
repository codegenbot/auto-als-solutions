int search(vector<int> lst){
    unordered_map<int, int> freqMap;
    for(int i : lst) {
        if(freqMap.find(i) == freqMap.end())
            freqMap[i] = 1;
        else
            freqMap[i]++;
    }
    int res = -1;
    for(auto p: freqMap) {
        if(p.second >= p.first && p.first > 0)
            res = p.first;
    }
    return res;
}