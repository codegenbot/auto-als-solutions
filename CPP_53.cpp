```cpp
int main() {
    int x, y;
    std::cout << "Enter first number: ";
    std::cin >> x;
    std::cout << "Enter second number: ";
    std::cin >> y;
    int sum = add(x, y);
    std::cout << "The sum is: " << sum << std::endl;
    return 0;
}

int add(int x, int y) {
    return x + y;
}