#include <iostream>
#include <vector>
#include <algorithm>
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
    for (int i = 0; i < a.size();i++){
        if (find(b.begin(), b.end(), a[i]) == b.end())
            return false;
    }
    return true;
}

int main(){
    vector<int> a = {4, 3, 2, 8};
    vector<int> b = {1,2,3,4};
    vector<int> result = common(a, b);
    for (auto x : result) {
        cout << x << " ";
    }
    cout << endl;
    assert(common(a, b) == vector<int>{2, 3});
}