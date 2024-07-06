#include <string>
#include <vector>
#include <iostream>

int main() {
    std::cout << "Enter some text: ";
    std::string text;
    std::getline(std::cin, text);

    if (text.empty()) {
        std::cout << "You must enter some text." << std::endl;
    } else {
        const char* c_str = text.c_str();
        std::string output = string_to_md5(c_str);
        std::cout << "MD5: " << output << std::endl;
    }

    return 0;
}