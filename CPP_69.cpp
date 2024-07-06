````
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
    for (auto it = freqMap.begin(); it != freqMap.end(); ++it) {
        if (it->second >= it->first && it->first > 0) {
            return it->first;
        }
    }
    return -1;
}

int main() {
    assert(findMaxValue({3, 10, 10, 9, 2}) == -1);
}