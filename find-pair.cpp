#include <vector>
using namespace std;

pair<int, int> findPair(vector<int>& numbers, int target) {
    unordered_map<int, int> numMap;
    for (int num : numbers) {
        int complement = target - num;
        if (numMap.count(complement)) {
            return {complement, num};
        }
        numMap[num] = 1;
    }
    return {{0, 0}}; // or throw an exception if no pair found
}