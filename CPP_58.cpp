```cpp
#include <iostream>
#include <vector>
#include <algorithm>

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
    for (int i = 0; i < a.size(); i++)
        if (find(b.begin(), b.end(), a[i]) == b.end())
            return false;
    return true;
}

int main(){
    vector<int> v1 = {4, 3, 2, 8};
    vector<int> v2 = {};
    cout << "Common elements: ";
    for(int x:v1)cout<<x<<" ";
    cout<<endl;
    vector<int> result = common(v1,v2);
    cout << "Vector 1 and Vector 2 are same: " << (issame(v1, v2)? "true" : "false") << endl;
}