#include <vector>

bool issame(vector<float> a,vector<float>b){
    if(a.size()!=b.size())return false;
    for(int i=0;i<a.size();i++){
        if(a[i]!=b[i]) return false;
    }
    return true;
}

int main() {
    vector<float> result = get_positive({1, -2, 3});
    assert(issame(result, {1, 3}));
    return 0;
}