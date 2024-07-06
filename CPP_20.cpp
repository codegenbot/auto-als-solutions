#include <vector>
#include <algorithm>
#include <initializer_list>

bool issame(std::vector<float> a, std::vector<float> b) {
    return (a.size() == b.size()) && (std::equal(a.begin(), a.end(), b.begin()));
}

int find_closest_elements(const std::vector<float>& elements, const float& target_value) {
    int closest_index = -1;
    float min_diff = std::numeric_limits<float>::max();
    
    for(int i=0; i<elements.size(); i++) {
        if(std::abs(elements[i] - target_value) < min_diff) {
            min_diff = std::abs(elements[i] - target_value);
            closest_index = i;
        }
    }
    
    return closest_index;
}

int main() {
    assert(issame({1.1, 2.2, 3.1, 4.1, 5.1}, {2.2, 3.1}));
    return 0;
}