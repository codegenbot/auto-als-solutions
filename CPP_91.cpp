#include <iostream>
#include <string>

int is_bored(std::string S) {
    int count = 0;
    size_t pos = 0;
    while ((pos = S.find("I", pos)) != std::string::npos) {
        if (S.substr(pos, 1).find_first_of(".,!") == std::string::npos)
            count++; 
        pos += 1; 
    }
    return count; 

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);
    int result = is_bored(input);
    std::cout << "Number of 'I' without punctuation: " << result << "\n";
    return 0;