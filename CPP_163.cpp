```cpp
#include <vector>
#include <algorithm>

vector<int> generate_integers(int a, int b) {
    vector<int> result;
    for (int i = min(a, b); i <= max(a, b); i++) {
        if (i % 2 == 0) {
            result.push_back(i);
        }
    }
    return result;
}

int main() {
    assert(generate_integers(17, 89) == vector<int>());
    return 0;
}