#include <vector>
#include <algorithm>

bool same(vector<pair<int, int>> a, vector<pair<int, int>> b) {
    if (a.size() != b.size()) {
        return false;
    }
    for (int i = 0; i < a.size(); i++) {
        if (a[i].first != b[i].first || a[i].second != b[i].second) {
            return false;
        }
    }
    return true;
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
    
    int resultValue = nodes[0].first;
    return vector<int>(1, resultValue);
}