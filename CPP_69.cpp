#include <iostream>
#include <vector>
#include <map>

int findMaxValue(std::vector<int> numbers) {
    std::map<int, int> freqMap;
    for (int num : numbers) {
        if (freqMap.find(num) == freqMap.end()) {
            freqMap[num] = 1;
        } else {
            freqMap[num]++;
        }
    }
    int maxValue = -1;
    for (auto it = freqMap.begin(); it != freqMap.end(); ++it) {
        if (it->second >= it->first && it->first > 0) {
            maxValue = it->first;
            break;
        }
    }
    return maxValue;
}

int main() {
    assert(findMaxValue({3, 10, 10, 9, 2}) == 1);
    return 0;
}