#include <vector>
#include <iostream>
#include <string>

std::string camelCase(std::string s) {
    std::string result = "";
    bool firstWord = true;
    
    for (char c : s) {
        if (c == '-') {
            if (!firstWord)
                result += std::toupper(c);
            else
                firstWord = false;
        } 
        else if (c == ' ') {
            if (!firstWord)
                result += std::toupper(c);
            else
                firstWord = false;
        } 
        else {
            if (firstWord)
                result += std::toupper(c);  // Check if this is the first word
            else
                result += std::tolower(c);
            firstWord = false;
        }
    }
    
    if (firstWord) {  
        result += std::string(1, std::toupper(s[0])) + std::string(1, std::tolower(s[1]));
    }
    
    return result;
}

int main() {
    std::string s;
    std::cout << "Enter a string: ";
    std::cin >> s;
    std::cout << camelCase(s) << std::endl;
    return 0;
}