```cpp
#include <cassert>
bool any_int(float a, float b, float c) {
    assert(any_int(3.01f,4.f,7.f)==false);
    return (a == b + c || a == c + b || b == a + c || b == c + a || c == a + b || c == b + a);
}
int main() {
    return 0;
}