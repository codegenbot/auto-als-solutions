```cpp
#include <vector>
#include <algorithm>

bool same(vector<int> a, vector<int> b) {
    return a == b;
}

vector<int> extract(vector<int> arr) {
    vector<pair<int, int>> nodes;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0) {
            nodes.push_back({arr[i], i});
        }
    }
    
    if (nodes.empty()) {
        return {};
    }
    
    sort(nodes.begin(), nodes.end());
    
    vector<int> result;
    for (int i = 1; i < nodes.size(); i++) {
        if (same({nodes[i-1].first, nodes[i-1].second}, {nodes[i].first, nodes[i].second})) {
            return {};
        }
    }
    
    return {nodes[0].first};
}