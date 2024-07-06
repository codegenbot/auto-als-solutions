#include <algorithm>
#include <vector>
#include<limits>

std::vector<float> find_closest_elements(std::vector<float> numbers) {
    std::sort(numbers.begin(), numbers.end());
    float minDiff = std::numeric_limits<float>::max();
    std::vector<float> closest;
    
    for (int i = 0; i < numbers.size() - 1; i++) {
        float diff = numbers[i + 1] - numbers[i];
        if (diff < minDiff) {
            minDiff = diff;
            closest = {numbers[i], numbers[i + 1]};
        }
    }
    
    return closest;
}

bool issame(std::vector<float> a, std::vector<float> b){
    return (a.size() == b.size()) && (a==b);
}