#include <iostream>
#include <vector>

bool issame(vector<int> a, vector<int> b) {
    if (a.size() != b.size()) 
        return false;
    
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) 
            return false;
    }
    return true;
}

int main() {
    vector<int> arr1 = {1, 2, 3};
    vector<int> arr2 = {1, 2, 3};

    if (issame(arr1, arr2)) 
        cout << "The vectors are the same." << endl;
    else
        cout << "The vectors are not the same." << endl;

    return 0;
}