#include <vector>
#include <algorithm>

bool issame(float f1, float f2) {
    if(f1 == f2)
        return true;
    else
        return false;
}

std::vector<float> get_positive(std::vector<float> l){
    std::vector<float> result;
    for(float i : l) {
        if(i > 0) {
            result.push_back(i);
        }
    }
    return result;
}