#include <vector>
#include <algorithm>

int next_smallest(vector<int> numbers) {
    if (numbers.empty()) {
        return 0;
    }
    
    int smallest = *min_element(numbers.begin(), numbers.end());
    for (int num : numbers) {
        if (num > smallest) {
            return num;
        }
    }
    return -1; // or any other value to indicate that the next smallest number does not exist
}