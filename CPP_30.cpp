#include <vector>

std::vector<float> get_positive(std::vector<float> l) {
    std::vector<float> result;
    for (float num : l) {
        if (num > 0) {
            result.push_back(num);
        }
    }
    return result;
}

bool issame(std::vector<float> a, std::vector<float> b) {
    if(a.size()!=b.size())return false;
    for(int i=0;i<a.size();i++){
        if(a[i]!=b[i]) return false;
    }
    return true;
}

int main() {
    std::vector<float> result = get_positive({1, -2, 3});
    assert(issame(result, {1, 3}));
    return 0;
}