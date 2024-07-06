```cpp
#include <algorithm>
#include <vector>
#include <numeric>
#include <limits>

using namespace std;

bool operator==(const vector<float>& a, const vector<float>& b) {
    return a.size() == b.size() && equal(a.begin(), a.end(), b.begin());
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