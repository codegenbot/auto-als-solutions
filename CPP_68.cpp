```
#include <iostream>
#include <vector>

std::vector<int> pluck(const std::vector<int>& arr) {
    std::vector<int> result = {};
    int minEvenValueIndex = -1;
    int minEvenValue = INT_MAX;

    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0 && arr[i] < minEvenValue) {
            minEvenValue = arr[i];
            minEvenValueIndex = i;
        }
    }

    if (minEvenValue != INT_MAX) {
        result.push_back(minEvenValue);
        result.push_back(minEvenValueIndex);
    }

    return result;
}

int main() {
    std::vector<int> inputArray = {1, 2, 3, 4};
    std::vector<int> outputArray = pluck(inputArray);

    for (int i : outputArray) {
        std::cout << i << " ";
    }

    return 0;
}