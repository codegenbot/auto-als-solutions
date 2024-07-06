```cpp
#include <algorithm>
#include <vector>
#include <numeric>

bool operator==(const vector<float>& a, const vector<float>& b) {
    return a.size() == b.size() && equal(a.begin(), a.end(), b.begin());
}

int main() {
    // Your code here...
}