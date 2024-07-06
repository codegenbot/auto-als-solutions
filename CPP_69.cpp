#include <algorithm>
#include <vector>
using namespace std;

int search(const vector<int>& vec, int target) {
    return distance(vec.begin(), find(vec.begin(), vec.end(), target));
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
    
    assert(search(vector<int>({3, 10, 10, 9, 2}), 10) == distance(vec.begin(), vec.end()));
    return 0;
}