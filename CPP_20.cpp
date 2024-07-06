#include <algorithm>
#include <numeric>

bool operator==(const vector<float>& a, const vector<float>& b) {
    return a.size() == b.size() && equal(a.begin(), a.end(), b.begin());
}

vector<pair<float, float>> find_closest_elements(vector<vector<float>>& numbers) {
    sort(numbers.begin(), numbers.end());
    float min_diff = numeric_limits<float>::max();
    pair<float, float> closest_pair;
    
    for(int i = 0; i < numbers.size() - 1; ++i) {
        float diff = numbers[i + 1][1] - numbers[i][1];
        if(diff < min_diff) {
            min_diff = diff;
            closest_pair.first = numbers[i][0];
            closest_pair.second = numbers[i + 1][1];
        }
    }
    
    return {closest_pair};
}