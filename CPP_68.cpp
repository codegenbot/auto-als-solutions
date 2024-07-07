#include <iostream>
#include <vector>
using namespace std;

bool issame(vector<int> a,vector<int>b){
    if(a.size() != b.size()) return false;
    for(int i = 0; i<a.size(); i++){
        if(a[i] != b[i]) return false;
    }
    return true;
}

std::vector<int> pluck(std::vector<int> arr) {
    std::vector<pair<int, int>> nodes;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0) {
            nodes.push_back({arr[i], i});
        }
    }
    if (nodes.empty()) {
        return {};
    }
    sort(nodes.begin(), nodes.end());
    return {nodes[0].first, nodes[0].second};
}

int main() {
    assert(issame(pluck({7, 9, 7, 1}), {}));
    cout << "No errors." << endl;
    return 0;
}