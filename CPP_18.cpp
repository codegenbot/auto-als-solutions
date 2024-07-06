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

    int main() {
        std::string inputStr, subStr;
        std::cout << "Enter a string: ";
        std::getline(std::cin, inputStr);
        std::cout << "Enter a substring: ";
        std::getline(std::cin, subStr);

        int result = how_many_times(inputStr, subStr);
        std::cout << "The substring appears " << result << " times.\n";
    }
}