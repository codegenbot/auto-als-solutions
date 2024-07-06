#include <algorithm>

vector<float> find_closest_elements(vector<float> numbers) {
    sort(numbers.begin(), numbers.end());
    float minDiff = numeric_limits<float>::max();
    vector<float> closest;
    
    for (int i = 0; i < numbers.size() - 1; i++) {
        float diff = numbers[i + 1] - numbers[i];
        if (diff < minDiff) {
            minDiff = diff;
            closest = {numbers[i], numbers[i + 1]};
        }
    }
    
    return closest;
}