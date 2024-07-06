int main 
{
    std::cout << "Enter a string: ";
    std::string S;
    std::cin >> S;
    int count = 0;
    size_t pos = 0;
    while ((pos = S.find("I", pos)) != std::string::npos) {
        if (S.find(".", pos) == std::string::npos && S.find("?", pos) == std::string::npos && S.find("!", pos) == std::string::npos)
            count++;
        pos = S.find(". ", pos) + 1; 
    }
    std::cout << "The string has " << count << " bored sentences.\n";
}