int main() {
    int x, y;
    std::cout << "Enter first number: ";
    std::cin >> x;
    std::cout << "Enter second number: ";
    std::cin >> y;
    int sum = add(x, y);
    std::cout << "Sum of the numbers is: " << sum << std::endl;
    return 0;
}