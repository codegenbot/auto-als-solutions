```
#include <cassert>

bool any_int(float a, float b, float c) {
    if (a == int(a) && b == int(b) && c == int(c)) {
        return a == b + c || a == c + b || b == a + c || b == c + a || c == a + b;
    }
    return false;
}

int main() {
    assert(any_int(3.01, 4, 7) == false);
    if (any_int(1.0, 2.0, 3.0)) {
        std::cout << "Triangle" << std::endl;
    } else {
        std::cout << "Not a Triangle" << std::endl;
    }
    return 0;
}