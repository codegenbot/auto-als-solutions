```cpp
#include <cassert>
bool any_int(float a, float b, float c) {
    assert(any_int(3.01f,4.f,7.f)==false);
    return (a == static_cast<int>(a) && (b == static_cast<int>(b) || c == static_cast<int>(c))) ||
           (b == static_cast<int>(b) && (a == static_cast<int>(a) || c == static_cast<int>(c))) ||
           (c == static_cast<int>(c) && (a == static_cast<int>(a) || b == static_cast<int>(b)));
}
int main() {
    return 0;
}