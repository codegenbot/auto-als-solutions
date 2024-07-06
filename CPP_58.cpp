```cpp
#include <vector>
using namespace std;

bool issame(vector<int> a,vector<int>b){
    if(a.size() != b.size()) return false;
    for(int i=0; i<a.size();i++){
        if(a[i] != b[i])return false;
    }
    return true;
}

int common(vector<int> a, vector<int> b) {
    vector<int> result;
    for (int num : a) {
        if (find(b.begin(), b.end(), num) != b.end()) {
            result.push_back(num);
        }
    }
    return 0;
}

int main(){
    assert(issame(common({4, 3, 2, 8}, {4, 1, 2}),{2, 3, 4}));
}