#include <algorithm>
#include <cmath>

int findMax(int n) {
    vector<int> l;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        l.push_back(num);
    }
    return *max_element(l.begin(), l.end());
}