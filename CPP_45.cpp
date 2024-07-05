```cpp
float triangle_area(int a, int h) {
    return (float)a * h / 2.0f;
}

int main() {
    printf("%f", triangle_area(10, 8));
    return 0;
}