#include <vector>
#include <iostream>

using namespace std;

pair<vector<int>, vector<int>> cutVector(vector<int> v) {
    int minDiff = INT_MAX;
    int idx = 0;
    
    for(int i = 1; i < v.size(); i++) {
        int diff = abs(v[i] - v[i-1]);
        
        if(diff <= minDiff) {
            minDiff = diff;
            idx = i;
        }
    }
    
    vector<int> left = vector<int>(v.begin(), v.begin() + idx);
    vector<int> right = vector<int>(v.begin() + idx, v.end());
    
    return make_pair(left, right);
}

int main() {
    int n;
    cin >> n;
    vector<int> v(n);
    
    for(int i = 0; i < n; i++) {
        cin >> v[i];
    }
    
    pair<vector<int>, vector<int>> res = cutVector(v);
    
    cout << "<";
    for(auto x : res.first) {
        cout << x << " ";
    }
    cout << ">" << endl;
    
    cout << "<";
    for(auto x : res.second) {
        cout << x << " ";
    }
    cout << "0" << endl;
    
    return 0;
}