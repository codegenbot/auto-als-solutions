#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> common(vector<int> a, vector<int> b){
    vector<int> result;
    for(auto x : a){
        if(find(b.begin(), b.end(), x) != b.end()) result.push_back(x);
    }
    return result;
}

int main(){
    vector<int> a = {4, 3, 2, 8};
    vector<int> b = {1,2,3,4};
    vector<int> result = common(a, b);
    for (auto x : result) {
        cout << x << " ";
    }
    cout << endl;
}