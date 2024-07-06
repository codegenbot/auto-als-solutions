```cpp
int add(int x, int y) {
    return x + y;
}

int main() {
    int num1, num2;
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;
    cout << "Sum: " << add(num1, num2);
    return 0;
}