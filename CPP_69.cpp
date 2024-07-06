#include <algorithm>
#include <vector>
using namespace std;

int search(const vector<int>& vec, int target) {
    return (find(vec.begin(), vec.end(), target) != vec.end()) ? distance(vec.begin(), find(vec.begin(), vec.end(), target)) : -1;
}

int main() {
    vector<int> vec;
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    vec.resize(n);
    
    cout << "Enter the elements: ";
    for(int i = 0; i < n; i++)
        cin >> vec[i];
    
    assert(find(vec.begin(), vec.end(), 10) != vec.end() ? distance(vec.begin(), find(vec.end(), 10)) : -1, "Element not found");
    return 0;
}