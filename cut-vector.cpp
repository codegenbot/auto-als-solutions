#include <vector>
using namespace std;

pair<vector<int>, vector<int>> cutVector(vector<int> vec) {
    int min_diff = INT_MAX;
    int cut_idx = 0;
    for (int i = 1; i < vec.size(); ++i) {
        int diff = abs(vec[i] - vec[0]);
        if (diff <= min_diff) {
            min_diff = diff;
            cut_idx = i;
        }
    }
    return {vector<int>(vec.begin(), vec.begin() + cut_idx), vector<int>(vec.begin() + cut_idx, vec.end())};
}

int main() {
    int n;
    cin >> n;
    vector<int> vec(n);
    for (auto &x : vec) cin >> x;
    
    pair<vector<int>, vector<int>> result = cutVector(vec);

    cout << "[";
    for (int x : result.first) cout << x << " ";
    cout << "] [";

    for (int x : result.second) cout << x << " ";

    cout << "]" << endl;

    return 0;
}