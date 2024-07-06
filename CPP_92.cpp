Here is the completed code:

bool any_int(float a, float b, float c) {
    if (abs(a - round(a)) < 0.001 && abs(b - round(b)) < 0.001 && abs(c - round(c)) < 0.001) {
        return (a == b + c || a == c + b || a == b - c || a == c - b);
    }
    return false;
}