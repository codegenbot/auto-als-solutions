#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> cutVector(vector<int> v) {
    int n = v.size();
    vector<vector<int>> res;
    
    int diffL = INT_MAX, diffR = INT_MAX; // Initialize maximum difference
    
    for (int i = 0; i < n; i++) {
        if (i == 0 || (v[i] - v[i-1]) > diffL) {
            res.push_back({v[i]});
            diffL = 0;
        } else if (i == n - 1 || (v[n-i-1] - v[i+1]) > diffR) {
            vector<int> temp = {v[i]};
            for(int j = i; j < n; j++) {
                if((v[j] - v[i]) > diffR) break;
                temp.push_back(v[j]);
            }
            res.push_back(temp);
            diffR = 0;
        } else if ((v[i] - (v[0]+v[n-1]))/2.0 < min(diffL, diffR)) {
            res.clear();
            res.push_back({v[0]});
            for(int j = 1; j < n; j++) {
                if((v[j] - v[0]) > diffL) break;
                res.back().push_back(v[j]);
            }
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