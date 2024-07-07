#include <vector>
using namespace std;

vector<vector<int>> cutVector(vector<int> v) {
    int n = v.size();
    vector<vector<int>> result;
    
    for (int i = 0; i < n - 1; i++) {
        if (v[i] == v[i + 1]) {
            result.push_back({v[i]});
            return {{}, {v[i], v[i+1]}};
        }
    }
    
    int minDiff = INT_MAX, index;
    for (int i = 0; i < n - 1; i++) {
        if (abs(v[i] - v[i + 1]) < minDiff) {
            minDiff = abs(v[i] - v[i+1]);
            index = i;
        }
    }
    
    result.push_back({v[0], v[index]});
    return {{v.begin() + (index + 1)}, {v.begin(), v.begin() + (index + 1)}};
}