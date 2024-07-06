```cpp
#include <vector>
#include <cassert>

using namespace std;

vector<int> common(vector<int> a, vector<int> b){
    vector<int> result;
    for(int i=0; i<a.size();i++){
        if(find(b.begin(),b.end(),a[i])!=b.end())result.push_back(a[i]);
    }
    return result;
}

bool issame(vector<int> a, vector<int> b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i < a.size();i++)
        if (find(b.begin(), b.end(), a[i]) == b.end())
            return false;
    return true;
}

int main(){
    vector<int> v1={4, 3, 2, 8};
    vector<int> v2={};
    assert(common(v1,v2) == v2);
}