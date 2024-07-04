#include <vector>
#include <iostream>
#include <numeric>
#include <cmath>
#include <climits>
using namespace std;

void cutVector(const vector<int>& vec) {
    int n = vec.size();
    int totalSum = accumulate(vec.begin(), vec.end(), 0);
    int leftSum = 0, minDiff = INT_MAX, cutIndex = 0;

    for (int i = 0; i < n - 1; ++i) {
        leftSum += vec[i];
        int rightSum = totalSum - leftSum;
        int diff = abs(leftSum - rightSum);
        if (diff < minDiff) {
            minDiff = diff;
            cutIndex = i + 1;
        }
    }

    cout << cutIndex << endl; // Added line to print cutIndex

    for (int i = 0; i < cutIndex; ++i) {
        cout << vec[i] << " ";
    }
    cout << endl;
    for (int i = cutIndex; i < n; ++i) {
        cout << vec[i] << " ";
    }
    cout << endl;
}

int main() {
    int n;
    cin >> n;
    vector<int> vec(n);
    for (int i = 0; i < n; ++i) {
        cin >> vec[i];
    }
    cutVector(vec);
    return 0;
}