int is_bored(std::string S) {
    int count = 0;
    size_t pos = 0;
    while ((pos = S.find("I", pos)) != std::string::npos) {
        if (S.find(".", pos + 1) == std::string::npos && 
            S.find("?", pos + 1) == std::string::npos && 
            S.find("!", pos + 1) == std::string::npos)
            count++;
        else
            pos = S.find(".", pos) + 1;
    }
    return count;
}