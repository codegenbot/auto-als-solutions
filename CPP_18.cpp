```
#include <iostream>
#include <string>

int main() {
    int how_many_times(std::string str, std::string substring) {
        int count = 0;
        size_t pos = 0;
        while ((pos = str.find(substring)) != std::string::npos) {
            count++;
            str.erase(0, pos + substring.size());
        }
        return count;
    }

    std::cout << "Enter a string: ";
    std::string input;
    std::cin >> input;

    std::cout << "Enter a substring: ";
    std::string subinput;
    std::cin >> subinput;

    int result = how_many_times(input, subinput);
    std::cout << "The substring appears " << result << " times." << std::endl;

    return 0;
}