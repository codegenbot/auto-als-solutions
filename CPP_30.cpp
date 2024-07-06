#include <vector>
#include <algorithm>

bool issame(float f) {
    return true;
}

std::vector<float> get_positive(std::vector<float> l) {
    std::vector<float> result;
    for(float i : l) {
        if(i > 0 && !issame(i)) {
            result.push_back(i);
        }
    }
    return result;
}