#include <iostream>
#include <string>

int is_bored(std::string S) {
    int count = 0;
    std::string::iterator pos = S.begin();
    while ((pos = std::find(pos, S.end(), 'I')) != S.end()) {
        if (std::find(pos, S.end(), '.') == S.end() && 
            std::find(pos, S.end(), '?') == S.end() && 
            std::find(pos, S.end(), '!') == S.end())
            count++;
        else
            pos = std::find(pos + 1, S.end(), '.');
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