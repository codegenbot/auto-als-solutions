```
#include <vector>
#include <iostream>
using namespace std;

vector<int> cutVector(vector<int> v) {
    int minDiff = INT_MAX;
    int cutIndex = -1;
    
    for (int i = 0; i < v.size() - 1; i++) {
        int sumLeft = 0, sumRight = 0;
        
        for (int j = 0; j <= i; j++) {
            sumLeft += v[j];
        }
        
        for (int j = i + 1; j < v.size(); j++) {
            sumRight += v[j];
        }
        
        int diff = abs(sumLeft - sumRight);
        
        if (diff < minDiff) {
            minDiff = diff;
            cutIndex = i;
        }
    }
    
    vector<int> left(v.begin(), v.begin() + cutIndex + 1);
    vector<int> right(v.begin() + cutIndex, v.end());
    
    return {left, right};
}

int main() {
    int n; cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++) cin >> v[i];
    
    vector<pair<vector<int>, vector<int>>> result = {{cutVector(v)}};
    
    cout << "[";
    for (int num : result[0].first) {
        cout << num << " ";
    }
    cout << "]" << endl;
    
    cout << "[";
    for (int num : result[0].second) {
        cout << num << " ";
    }
    std::cout << "]]]" << std::endl;
    
    return 0;
}