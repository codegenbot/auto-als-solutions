#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> cutVector(vector<int> v) {
    int n = v.size();
    vector<vector<int>> res;
    int min_diff = INT_MAX;

    for (int i = 0; i < n; i++) {
        if (i == 0 || abs(v[i] - v[i-1]) > min_diff) {
            res.push_back({v[i]});
            min_diff = abs(v[i] - v[i]);
        } else if (i == n - 1 || abs(v[i] - v[i+1]) > min_diff) {
            res.back().push_back(v[i]);
        }
    }

    return res;
}

int main() {
    int n;
    cin >> n;

    vector<int> v(n);
    for (auto& x : v) {
        cin >> x;
    }

    vector<vector<int>> res = cutVector(v);

    for (const auto& x : res) {
        for (int y : x) {
            cout << y << " ";
        }
        cout << endl;
    }

    return 0;
}