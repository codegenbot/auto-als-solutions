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
        std::string str;
        std::string substring;

        std::cout << "Enter the string: ";
        std::getline(std::cin, str);

        std::cout << "Enter the substring: ";
        std::getline(std::cin, substring);

        int count = how_many_times(str, substring);
        std::cout << "The substring appears " << count << " times." << std::endl;

        return 0;
    }