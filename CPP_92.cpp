```cpp
bool any_int(float a, float b, float c) {
    int ai = (int)a, bi = (int)b, ci = (int)c;
    return ai == bi + ci || bi == ai + ci || ci == ai + bi;
}

int main() {
    assert(any_int(3.01f, 4, 7) == false);
    return 0;
}