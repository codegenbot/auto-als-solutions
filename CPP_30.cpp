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
    assert(issame(get_positive({}), {}));
    return 0;
}

vector<float> get_positive(vector<float> l){
    vector<float> result;
    for(float num : l) {
        if(num > 0) {
            result.push_back(num);
        }
    }
    return result;
}