```cpp
bool any_int(float a, float b, float c) {
    int ai = (int)a;
    int bi = (int)b;
    int ci = (int)c;

    return a == bi + ci || b == ai + ci || c == ai + bi;
}

int main() {
    assert(any_int(3.01f, 4.f, 7.f) == false);
}