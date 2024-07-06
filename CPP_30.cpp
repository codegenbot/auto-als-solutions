#include <vector>
#include <algorithm>

bool issame(vector<float> l1, vector<float> l2) {
    if(l1.size() != l2.size()) 
        return false;
    for(float num : l1) {
        if(std::find(l2.begin(), l2.end(), num) == l2.end())
            return false;
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