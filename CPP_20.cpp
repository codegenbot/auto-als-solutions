```cpp
#include <vector>
#include <algorithm>

float find_closest_elements(float a, float b) {
    return std::abs(a - b);
}

bool issame(const std::vector<float>& a, const std::vector<float>& b) {
    int la = a.size();
    int lb = b.size();
    
    for(int i = 0; i < la && i < lb; i++) {
        if(find_closest_elements(a[i], b[i]) > 0.0001) return false;
    }
    
    return true;
}