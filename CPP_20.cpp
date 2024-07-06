#include <initializer_list>
#include <vector>
#include <algorithm>

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
    assert(issame({1.1f, 2.2f, 3.1f, 4.1f, 5.1f}, {2.2f, 3.1f}));
    return 0;
}