```cpp
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    vector<int> vec;
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        int x;
        cin >> x;
        vec.push_back(x);
    }
    assert(std::find(vec.begin(), vec.end(), 1) != vec.end());
    return 0;
}