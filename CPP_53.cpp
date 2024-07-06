int add(int x, int y) {
    return x + y;
}

int main() {
    int num1, num2;
    std::cout << "Enter the first number: ";
    std::cin >> num1;
    std::cout << "Enter the second number: ";
    std::cin >> num2;
    int sum = add(num1, num2);
    std::cout << "The sum is: " << sum << std::endl;
    return 0;
}