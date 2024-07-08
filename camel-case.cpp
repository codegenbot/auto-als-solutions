std::string camelCase(std::string s) {
    std::string result = "";
    bool firstWord = true;
    
    for (char c : s) {
        if (c == '-') {
            result += std::toupper(c);
            firstWord = false;
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
                result += std::tolower(c);
            firstWord = false;
        }
    }
    
    if (!firstWord) {  // Handle the last word separately
        result[0] = std::tolower(result[0]);
    }
    
    return result;
}