#include <vector>
#include <algorithm>

float find_closest_elements(float a, float b) {
    if(a > b)
        return a - b;
    else
        return b - a;
}

bool issame(const std::vector<float>& a, const std::vector<float>& b) {
    if(a.size() != b.size()) 
        return false;

    for(int i = 0; i < a.size(); i++) {
        float diff = find_closest_elements(a[i], b[i]);
        if(diff > 1e-9)
            return false;
    }

    return true;
}