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
                result += c;
            firstWord = false;
        }
    }
    
    if (firstWord) {  // Handle the first word separately
        result = std::string(1, std::toupper(s[0])) + std::tolower(std::string(s.begin()+1, s.end()));
    }
    
    return result;