int main 
{
    std::string S;
    int count = 0;
    size_t pos = 0;
    std::cout << "Enter a string: ";
    std::getline(std::cin, S);
    while ((pos = S.find("I", pos)) != std::string::npos) {
        if (S.find(".", pos) == std::string::npos && S.find("?", pos) == std::string::npos && S.find("!", pos) == std::string::npos)
            count++;
        pos = S.find(". ", pos) + 1; 
    }
    std::cout << "Number of times 'I' is used without punctuation: " << count;
}