```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;

vector<int> common(vector<int> a, vector<int> b){
    vector<int> result;
    for(int i=0; i<a.size();i++){
        auto it = find(b.begin(),b.end(),a[i]);
        if(it != b.end())result.push_back(*it);
    }
    return result;
}

bool issame(vector<int> a, vector<int> b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i < a.size(); i++)
        if (find(b.begin(), b.end(), a[i]) == b.end())
            return false;
    return true;
}

int main(){
    assert(common({4, 3, 2, 8}, {}) == {});
}