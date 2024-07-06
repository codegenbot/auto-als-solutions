#include <vector>
#include <algorithm>

bool issame(float x1, float x2) {
    return (x1 - x2) <= 0.0001;
}

std::vector<float> get_positive(std::vector<float> l) {
    std::vector<float> result;
    for(float i : l) {
        if(i > 0 || issame(0, i)) {
            result.push_back(i);
        }
    }
    return result;
}