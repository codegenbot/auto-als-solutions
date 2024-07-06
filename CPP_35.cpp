#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> l(n);
    for(int i = 0; i < n; i++) {
        cin >> l[i];
    }
    cout << *max_element(l.begin(), l.end()) << endl;
    return 0;
}