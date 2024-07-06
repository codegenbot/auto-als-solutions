int main{
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);
    std::cout << flip_case(input) << std::endl;
    return 0;