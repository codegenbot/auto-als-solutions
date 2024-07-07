#include <vector>
using namespace std;

vector<vector<int>> cutVector(vector<int> v) {
    int minDiff = INT_MAX;
    int cutIndex = 0;
    vector<vector<int>> result(2);

    for (int i = 1; i < v.size(); i++) {
        int diff = abs(v[i] - v[i-1]);
        if (diff <= minDiff) {
            minDiff = diff;
            cutIndex = i;
        }
    }

    result[0].insert(result[0].end(), v.begin(), v.begin() + cutIndex);
    result[1].insert(result[1].begin(), v.begin() + cutIndex, v.end());

    return result;
}

int main() {
    int n;
    cin >> n;

    vector<int> v(n+1);
    for (int i = 0; i <= n; i++) {
        cin >> v[i];
    }

    vector<vector<int>> res = cutVector(v);

    for (const auto &subVec : res) {
        for (int num : subVec) {
            cout << num << " ";
        }
        cout << endl;
    }

    return 0;
}