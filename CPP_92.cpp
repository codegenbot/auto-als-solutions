Here is the solution:

bool any_int(float a, float b, float c) {
    if (abs(a - (b + c)) < 1e-6 && a == static_cast<int>(a)) {
        return true;
    }
    if (abs(b - (a + c)) < 1e-6 && b == static_cast<int>(b)) {
        return true;
    }
    if (abs(c - (a + b)) < 1e-6 && c == static_cast<int>(c)) {
        return true;
    }
    return false;