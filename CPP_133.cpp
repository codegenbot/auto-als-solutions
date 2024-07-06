int main() {
    std::vector<double> lst;
    double num;

    while ((std::cin >> num) && (!std::cin.peek())) { 
        lst.push_back(num);
    }

    int sum = sum_squares(lst);

    std::cout << "Sum of squares: " << sum << std::endl;
    return 0;
}