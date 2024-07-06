int main() {
    int x, y;
    std::cout << "Enter first number: ";
    std::cin >> x;
    std::cout << "Enter second number: ";
    std::cin >> y;
    int result = add(x, y);
    std::cout << "The sum is: " << result << std::endl;
    return 0;
}