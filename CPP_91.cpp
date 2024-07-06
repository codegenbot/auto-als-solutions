#include <iostream>
#include <string>

int is_bored(std::string S) {
    int count = 0;
    size_t prev_pos = 0;
    while ((size_t pos = S.find("I", prev_pos)) != std::string::npos) {
        if (pos == 0 || S[pos - 1] != '.' && S[pos - 1] != '?' && S[pos - 1] != '!') 
            count++;
        prev_pos = pos + 1;
    }
    return count;

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);
    int result = is_bored(input);
    std::cout << "Number of 'I' without punctuation: " << result << "\n";
    return 0;
}