#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    vector<int> l;
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        int x;
        cin >> x;
        l.push_back(x);
    }
    cout << *max_element(l.begin(), l.end()) << endl;
    return 0;
}