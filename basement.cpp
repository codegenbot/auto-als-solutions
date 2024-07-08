```cpp
#include <vector>
using namespace std;

int basement(vector<int>& v) {
    int sum = 0;
    for (int i = 0; i < v.size(); i++) {
        sum += v[i];
        if (sum < 0)
            return i;
    }
    return -1; // not found
}

int main() {
    vector<int> v = {1, -2, 3, 4, -5};
    cout << basement(v) << endl;
    return 0;
}