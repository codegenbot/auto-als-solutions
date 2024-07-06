```cpp
#include <vector>
#include <limits>
#include <cmath>

bool isSame(vector<float> a, vector<float> b) {
    // implementation
}

vector<pair<float, float>> find_closest_elements(vector<float> numbers) {
    if (numbers.size() < 2) {
        return {{numeric_limits<float>::min(), numeric_limits<float>::max()}};
    }
    
    float min_diff = numeric_limits<float>::max();
    pair<float, float> closest_pair;
    
    for (int i = 0; i < numbers.size(); ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            float diff = abs(numbers[i] - numbers[j]);
            if (diff < min_diff) {
                min_diff = diff;
                closest_pair = {numbers[i], numbers[j]};
            }
        }
    }
    
    return {{closest_pair.first, closest_pair.second}};
}

int main() {
    assert(isSame(find_closest_elements({1.1, 2.2, 3.1, 4.1, 5.1}), {2.2, 3.1}));
    return 0;
}