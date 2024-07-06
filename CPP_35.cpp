#include <algorithm>

int main() {
    vector<int> l;
    // read input from user
    int n;
    cin >> n;
    for(int i=0; i<n; i++) {
        int x;
        cin >> x;
        l.push_back(x);
    }
    
    return *std::max_element(l.begin(), l.end());
}