```cpp
#include <cassert>

bool any_int(float a, float b, float c) {
    if (a == int(a) && b == int(b) && c == int(c)) {
        return a == int(a) + int(b) || a == int(b) + int(c) || int(b) == a + int(c) || int(b) == int(c) + int(a) || int(c) == a + int(b);
    }
    return false;
}

int main() {
    assert(any_int(3.01, 4, 7) == false);
    return 0;
}