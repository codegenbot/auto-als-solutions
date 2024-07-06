```
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool same(vector<int> a, vector<int> b) {
    if (a.size() != b.size()) return false;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) return false;
    }
    return true;
}

vector<int> maximum(vector<int> arr, int k) {
    vector<int> result;
    for (int i = 0; i < k; i++) {
        auto it = max_element(arr.begin(), arr.end());
        result.push_back(*it);
        arr.erase(it);
    }
    return result;
}

int main() {
    int n, k;
    cout << "Enter the number of elements: ";
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cout << "Enter k: ";
    cin >> k;
    if(k > n) k = n;
    vector<int> result = maximum(arr, k);
    if(same(result, vector<int>(k, 243))) {
        cout << "Maximum values are equal.\n";
    } else {
        cout << "Maximum values are not equal.\n";
    }
}