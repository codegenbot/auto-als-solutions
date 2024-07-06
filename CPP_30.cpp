#include <vector>
#include <algorithm>

bool issame(vector<float> v1, vector<float> v2) {
    if(v1.size() != v2.size()) {
        return false;
    }
    
    for(int i = 0; i < v1.size(); i++) {
        if(std::abs(v1[i] - v2[i]) > 0.00001f) {
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