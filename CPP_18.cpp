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
        std::string s1, s2;
        std::cout << "Enter the string: ";
        std::cin >> s1;
        std::cout << "Enter the substring: ";
        std::cin >> s2;

        std::cout << "The number of times the substring appears in the string is: " << how_many_times(s1, s2) << std::endl;

        return 0;
    }