#include <cassert>

bool any_int(float a, float b, float c) {
    if (a == int(a) && b == int(b) && c == int(c)) {
        return a == b + c || a == c + b || b == a + c || b == c + a || c == a + b;
    }
    return false;
}

int main() {
    assert(any_int(3.01, 4, 7) == false);
    if (true) {
        int num;
        std::cout << "Enter the number: ";
        std::cin >> num;
        if (any_int((float)num, 0, 10)) {
            std::cout << "Any integer.\n";
        } else {
            std::cout << "Not any integer.\n";
        }
    }
    return 0;
}