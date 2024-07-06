```
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

bool isSame(vector<int> a, vector<int> b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i < a.size(); i++)
        if (find(b.begin(), b.end(), a[i]) == b.end())
            return false;
    return true;
}

int main(){
    assert(isSame({4, 3, 2, 8}, {1,2,3,4}) && "Test failed");
    cout << common({4, 3, 2, 8}, {1,2,3,4}).size()<< endl;
}