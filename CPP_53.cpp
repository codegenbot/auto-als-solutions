int main() {
    int num1, num2;
    std::cout << "Enter two numbers: ";
    std::cin >> num1 >> num2;
    int sum = add(num1, num2);
    std::cout << "Sum of the numbers is: " << sum << std::endl;
    return 0;
}