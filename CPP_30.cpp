#include <iostream>
#include <vector>

bool issame(float l1, float r1, float l2, float r2) {
    if(l1 == l2 && r1 == r2)
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