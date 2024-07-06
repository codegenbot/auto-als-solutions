```cpp
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    vector<int> vec;
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    vec.resize(n);
    
    cout << "Enter the elements: ";
    for(int i = 0; i < n; i++)
        cin >> vec[i];
    
    int result = std::distance(vec.begin(), std::find(vec.begin(), vec.end(), vec[0]));
    assert(result == vec.size());
    return 0;
}