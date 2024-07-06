#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> unique(vector<int> l) {
    vector<int> result(l.begin(), l.end());
    sort(result.begin(), result.end());
    return result;
}

int main() {
    vector<int> v = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    for (int x : v) {
        cout << x << " ";
    }
    cout << endl;
    
    vector<int> unique_v = unique(v);
    for (int x : unique_v) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}