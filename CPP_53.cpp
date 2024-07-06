int add(int x, int y) {
    return x + y;
}

int main() {
    int a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;
    cout << "Sum: " << add(a, b);
}