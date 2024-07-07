#include <iostream>
#include <vector>

bool issame(vector<int> a, vector<int> b) {
    if (a.size() != b.size()) {
        return false;
    }
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}

vector<int> maximum(vector<int> arr, int k) {
    vector<int> result;
    for (int i = 0; i < k; i++) {
        auto it = std::max_element(arr.begin(), arr.end());
        result.push_back(*it);
        arr.erase(it);
    }
    return result;
}

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    vector<int> res = maximum(arr, k);

    cout << "Maximum values: ";
    for (int i = 0; i < k; i++) {
        cout << res[i] << " ";
    }
    cout << endl;

    return 0;
}