result middleCharacter(string str) {
    int len = str.length();
    if(len % 2 == 0) {
        return std::string(1, str.substr(len/2 - 1, 2).at(0));
    } else {
        return std::string(1, str[len/2]);
    }
}