#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> cutVector(vector<int> v) {
    int n = v.size();
    vector<vector<int>> res;
    
    for (int i = 0; i < n; i++) {
        if (i == 0 || v[i] > v[i - 1]) {
            res.push_back({v[i]});
        } else if (i == n - 1 || v[i] < v[i + 1]) {
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