```c++
std::string camelCase(std::string s) {
    std::string result;
    bool firstWord = true;

    for (char c : s) {
        if (c == '-') {
            // skip '-'
        } 
        else if (c == ' ') {
            if (!firstWord)
                result += c;
            firstWord = false;
        } 
        else {
            if (firstWord)
                result += std::toupper(c);  // Check if this is the first word
            else
                result += c;  // If not the first word, just add as it is
            firstWord = false;
        }
    }
    
    // Handle the last word separately
    if (result.size() > 0 && !std::isupper(result[0])) {
        result[0] = std::tolower(result[0]);
    }
    
    return result;
}