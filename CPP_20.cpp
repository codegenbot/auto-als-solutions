#include <algorithm>
#include <numeric>
#include <vector>

bool operator==(const std::vector<float>& a, const std::vector<float>& b) {
    return a.size() == b.size() && equal(a.begin(), a.end(), b.begin());
}

int main() {
    // Your code to test the function
    vector<float> numbers = {0.5f, 0.8f, 1.2f, 1.5f};
    pair<float, float> closest_pair = find_closest_elements(numbers);
    
    return 0;
}

vector<float> find_closest_elements(vector<float> numbers) {
    sort(numbers.begin(), numbers.end());
    float min_diff = numeric_limits<float>::max();
    pair<float, float> closest_pair;
    
    for(int i = 0; i < numbers.size() - 1; ++i) {
        float diff = numbers[i + 1] - numbers[i];
        if(diff < min_diff) {
            min_diff = diff;
            closest_pair.first = numbers[i];
            closest_pair.second = numbers[i + 1];
        }
    }
    
    return {closest_pair.first, closest_pair.second};
}