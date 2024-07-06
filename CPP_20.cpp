#include <vector>
#include <algorithm>

bool issame(std::vector<float> a, std::vector<float> b) {
    return (a.size() == b.size()) && (std::equal(a.begin(), a.end(), b.begin()));
}

float find_closest_elements(const std::vector<float>& arr1, const std::vector<float>& arr2) {
    float min_diff = FLT_MAX;
    int idx = -1;

    for(int i=0; i<arr1.size(); i++) {
        for(int j=0; j<arr2.size(); j++) {
            if(abs(arr1[i]-arr2[j]) < min_diff) {
                min_diff = abs(arr1[i]-arr2[j]);
                idx = i;
            }
        }
    }

    return arr1[idx];
}

int main() {
    assert(issame(std::vector<float>(find_closest_elements({1.1, 2.2, 3.1, 4.1, 5.1}, {1.0, 2.0}), {1.1, 2.2, 3.1, 4.1, 5.1}) , {2.2, 3.1}));
    return 0;
}