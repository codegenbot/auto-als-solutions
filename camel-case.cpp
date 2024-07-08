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
    
    if (!s.empty() && !firstWord) {  // Handle the first word separately
        result[0] = std::tolower(result[0]);
    }
    
    return result;
}