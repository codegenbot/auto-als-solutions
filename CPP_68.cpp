#include <vector>
#include <algorithm>

bool issame(vector<pair<int, int>> a, vector<pair<int, int>> b) {
    if(a.size() != b.size()) return false;
    for(int i=0; i<a.size(); i++){
        if(a[i] != b[i]) return false;
    }
    return true;
}

vector<int> pluck(vector<int> arr) {
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
        if(issame(vector<pair<int, int>>({nodes[i-1].first, nodes[i-1].second}), 
                  vector<pair<int, int>>({nodes[i].first, nodes[i].second})) ) {
            continue;
        }
        result.push_back(nodes[i].first);
    }
    
    return result;
}