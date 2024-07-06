int add(int x, int y) {
    return x + y;
}

int main() {
    int num1, num2;
    std::cout << "Enter first number: ";
    std::cin >> num1;
    std::cout << "Enter second number: ";
    std::cin >> num2;
    std::cout << "Sum: " << add(num1, num2) << std::endl;
}