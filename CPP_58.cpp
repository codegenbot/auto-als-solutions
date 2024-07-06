```
#include <iostream>
#include <vector>
#include <set>

using namespace std;

bool issame(vector<int> v1, vector<int> v2) {
    if(v1.size() != v2.size()) return false;
    for(int i = 0; i < v1.size(); i++) {
        if(v1[i] != v2[i]) return false;
    }
    return true;
}

vector<int> common(vector<int> l1, vector<int> l2) {
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());
    set<int> intersection;
    
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
        inserter(intersection, intersection.begin()));
    
    vector<int> result(intersection.begin(), intersection.end());
    return result;
}

int main() {
    int n1, m1, n2, m2;
    cout << "Enter the size of first array: ";
    cin >> n1;
    cout << "Enter the elements of first array: ";
    vector<int> l1(n1);
    for(int i = 0; i < n1; i++) {
        cin >> l1[i];
    }
    
    cout << "Enter the size of second array: ";
    cin >> m2;
    cout << "Enter the elements of second array: ";
    vector<int> l2(m2);
    for(int i = 0; i < m2; i++) {
        cin >> l2[i];
    }
    
    if(issame(l1, l2)) {
        cout << "The arrays are same." << endl;
    } else {
        vector<int> common_array = common(l1, l2);
        cout << "Common elements: ";
        for(int i = 0; i < common_array.size(); i++) {
            cout << common_array[i] << " ";
        }
        cout << endl;
    }
    
    return 0;
}