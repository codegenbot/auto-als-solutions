#include <algorithm>
#include <cmath>

int findMax(int n) {
    vector<int> l;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        l.push_back(a);
    }
    return *max_element(l.begin(), l.end());
}