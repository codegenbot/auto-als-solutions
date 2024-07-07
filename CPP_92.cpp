#include <cassert>
#include <cmath>

bool any_int(float a, float b, float c);

bool any_int(float a, float b, float c) {
    if (a == static_cast<int>(a)) return (a == b + c || a == c + b);
    if (b == static_cast<int>(b)) return (b == a + c || b == c + a);
    if (c == static_cast<int>(c)) return (c == a + b || c == b + a);
    return false;
}

int main() {
    assert(any_int(3.01, 4, 7) == false);
    return 0;
}