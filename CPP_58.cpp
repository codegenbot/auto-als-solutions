```cpp
#include <iostream>
#include <vector>
#include <set>

using namespace std;

bool issame(vector<int> v1, vector<int> v2) {
    if(v1.size() != v2.size())
        return false;
    
    for(int i = 0; i < v1.size(); i++) {
        if(v1[i] != v2[i])
            return false;
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
    vector<int> v1 = {1, 2, 3, 4};
    vector<int> v2 = {2, 4, 6, 8};
    
    if(issame(v1, v2)) {
        cout << "Vectors are same" << endl;
    } else {
        cout << "Vectors are not same" << endl;
        
        vector<int> common_elements = common(v1, v2);
        
        for(int i = 0; i < common_elements.size(); i++) {
            cout << common_elements[i] << " ";
        }
        
        cout << endl;
    }
    
    return 0;
}