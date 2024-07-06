#include <iostream>
#include <string>

std::string flip_case(std::string str){
    std::string result = "";
    for (int i = 0; i < str.length(); i++) {
        char c = str[i];
        if (c >= 'a' && c <= 'z') 
            result += std::toupper(c);
        else if (c >= 'A' && c <= 'Z')
            result += std::tolower(c);
        else
            result += c;
    }
    return result;
}

int main() {
    std::string s;
    std::cout << "Enter a string: ";
    std::cin >> s;
    std::cout << "Flip Case: " << flip_case(s) << std::endl;
    return 0;
}