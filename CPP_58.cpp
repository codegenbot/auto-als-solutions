```cpp
#include <iostream>
#include <vector>
#include <set>

using namespace std;

bool issame(vector<int> v1, vector<int> v2) {
    if(v1.size() != v2.size()) return false;
    for(int i = 0; i < v1.size(); i++) {
        if(find(v2.begin(), v2.end(), v1[i]) == v2.end())
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
    int n1, m1, n2, m2;
    cin >> n1 >> m1;
    vector<int> l1(n1);
    for(int i = 0; i < n1; i++) 
        cin >> l1[i];
    cin >> n2 >> m2;
    vector<int> l2(n2);
    for(int i = 0; i < n2; i++) 
        cin >> l2[i];
    
    if(issame(l1, l2))
        cout << "The lists are same." << endl;
    else
        cout << "The lists are not same." << endl;
        
    vector<int> commonList = common(l1, l2);
    cout << "Common elements: ";
    for(int i = 0; i < commonList.size(); i++) 
        cout << commonList[i] << " ";
    cout << endl;
    
    return 0;
}