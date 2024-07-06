#include <algorithm>
#include <vector>
#include <numeric>

int findMaxValue(std::vector<int> numbers) {
    int maxVal = -1;
    for (int num : numbers) {
        if (num > maxVal) {
            maxVal = num;
        }
    }
    return maxVal;
}