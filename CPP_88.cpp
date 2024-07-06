```cpp
#include <vector>
#include <algorithm>

bool issame(const std::vector<int>& a) {
    for(int i = 1; i < a.size(); i++) {
        if (a[i-1] > a[i]) return false;
    }
    return true;
}

int main() {
    assert(issame({21, 14, 23, 11}));
    // Test your function with different inputs.
}