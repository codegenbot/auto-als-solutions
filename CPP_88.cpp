#include <vector>

bool issame(vector<int> a,vector<int>b){
    if(a.size()!=b.size()) return false;
    for(int i=0; i<a.size(); i++){
        if(a[i]!=b[b.size()-1-i]) return false;
    }
    return true;
}

int main() {
    vector<int> array = {21, 14, 23, 11};
    vector<int> result = sort_array(array);
    assert(issame(result,{23,21,14,11}));
    return 0;
}