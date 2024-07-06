#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int findMax(vector<int> l) {
    return *max_element(l.begin(), l.end());
}

int main() {
    int n;
    vector<int> l;
    
    cin >> n;
    for(int i=0; i<n; i++) {
        int x;
        cin >> x;
        l.push_back(x);
    }
    
    cout << findMax(l) << endl;

    return 0;
}