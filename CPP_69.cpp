#include <algorithm>
#include <vector>
using namespace std;

int findElement(const vector<int>& vec, int target) {
    return distance(vec.begin(), find(vec.begin(), vec.end(), target) - vec.begin());
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
    
    assert(find(vec.begin(), vec.end(), 10) != vec.end() ? findElement(vec, 10) : -1,  );
    return 0;
}