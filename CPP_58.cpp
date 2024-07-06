#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<int> common(vector<int> a, set<int> b){
    vector<int> result;
    for(int i=0; i<a.size();i++){
        if(b.count(a[i]))result.push_back(a[i]);
    }
    return result;
}

int main(){
    vector<int> a = {4, 3, 2, 8};
    set<int> b = {1,2,3,4};
    vector<int> result = common(a, b);
    for (auto x : result) {
        cout << x << " ";
    }
    cout << endl;
}