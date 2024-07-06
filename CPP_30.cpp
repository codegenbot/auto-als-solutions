#include <vector>
#include <iostream>

bool issame(vector<float> v1, vector<float> v2) {
    if(v1.size() != v2.size()) {
        return false;
    }
    
    for(float num : v1) {
        if(std::find(v2.begin(), v2.end(), num) == v2.end()) {
            return false;
        }
    }
    
    return true;
}

int main() {
    vector<float> l = {1.0, -2.0, 3.0};
    vector<float> result = get_positive(l);
    assert(issame(get_positive({}), {}));
    return 0;
}