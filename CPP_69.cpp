#include <iostream>
#include <map>
#include <vector>

int search(std::vector<int> lst) {
    std::map<int, int> freqMap;
    for (int num : lst) {
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
    std::vector<int> lst = {3, 10, 10, 9, 2};
    int result = search(lst);
    if (result != -1)
        std::cout << "First element greater than or equal to its frequency is: " << result << std::endl;
    else
        std::cout << "No such element found." << std::endl;
    return 0;
}