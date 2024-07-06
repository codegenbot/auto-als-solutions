#include <algorithm>
#include <vector>
using namespace std;

int search(const vector<int>& vec, int target) {
    auto it = find(vec.begin(), vec.end(), target);
    return it == vec.end() ? -1 : distance(it, vec.end());
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
    
    assert(search(vec, vec[0]) == -1);
    return 0;
}