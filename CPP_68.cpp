#include <vector>
#include <algorithm>

bool same(vector<pair<int, int>> a, vector<pair<int, int>> b) {
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
        return vector<int>();
    }
    
    sort(nodes.begin(), nodes.end());
    
    int result = nodes[0].first;
    return vector<int>(1, result);
}