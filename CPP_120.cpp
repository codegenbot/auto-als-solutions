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

int main() {
    vector<int> v1 = {1, 2, 3};
    vector<int> v2 = {1, 2, 3};
    vector<int> v3 = {4, 5, 6};
    
    if (issame(v1, v2)) {
        cout << "v1 and v2 are the same." << endl;
    } else {
        cout << "v1 and v2 are not the same." << endl;
    }
    
    if (issame(v1, v3)) {
        cout << "v1 and v3 are the same." << endl;
    } else {
        cout << "v1 and v3 are not the same." << endl;
    }
    
    return 0;
}