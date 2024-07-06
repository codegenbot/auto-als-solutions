char getEncryptedChar(char c) {
    if(c >= 'a' && c <= 'i') 
        return (c - 'a' + 26 - 2 * 2)%26 + 'a';
    else if(c >= 'j' && c <= 'n') 
        return (c - 'j' - 1 + 26 - 2 * 2)%26 + 'j';
    else if(c >= 'o' && c <= 'q') 
        return (c - 'o' - 3 + 26 - 2 * 2)%26 + 'o';
    else if(c >= 'r' && c <= 's') 
        return (c - 'r' - 4 + 26 - 2 * 2)%26 + 'r';
    else if(c >= 't' && c <= 'u') 
        return (c - 't' - 5 + 26 - 2 * 2)%26 + 't';
    else if(c >= 'v' && c <= 'w') 
        return (c - 'v' - 6 + 26 - 2 * 2)%26 + 'v';
    else if(c >= 'x' && c <= 'y') 
        return (c - 'x' - 7 + 26 - 2 * 2)%26 + 'x';
    else if(c == 'z') 
        return (c - 'a' + 25 - 2 * 2)%26 + 'a';    
}

string encrypt(string s) {
    string result = "";
    for(char c : s) {
        if(isalpha(c)) {
            if(toupper(c) >= 'A' && toupper(c) <= 'M') 
                result += getEncryptedChar(c);
            else if(toupper(c) >= 'N' && toupper(c) <= 'Z') 
                result += getEncryptedChar(c);
            else if(islower(c)) 
                result += tolower(getEncryptedChar(c));
            else 
                result += c;
        }
        else 
            result += c;
    }
    return result;
}