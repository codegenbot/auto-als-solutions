```cpp
#include <vector>
#include <algorithm>

bool issame(vector<int> a, vector<int> b) {
    return a == b;
}

vector<vector<int>> pluck(vector<int> arr) {
    vector<pair<int, int>> nodes;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0) {
            nodes.push_back({arr[i], i});
        }
    }
    
    if (nodes.empty()) {
        return {{}};
    }
    
    sort(nodes.begin(), nodes.end());
    
    vector<vector<int>> result;
    int prev = -1;
    for (int i = 0; i < nodes.size(); i++) {
        if (prev == nodes[i].second) continue;
        
        vector<int> temp;
        for (int j = max(0, nodes[i].second - 10); j <= min(arr.size() - 1, nodes[i].second + 11); j++) {
            temp.push_back(arr[j]);
        }
        
        result.push_back(temp);
        prev = nodes[i].second;
    }
    
    return result;
}