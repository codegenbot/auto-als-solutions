#include <algorithm>
#include <vector>
#include <limits>

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
    if(a.size() != b.size())
        return false;
    for(int i = 0; i < a.size(); i++){
        if(abs(a[i] - b[i]) > 1e-5)
            return false;
    }
    return true;
}