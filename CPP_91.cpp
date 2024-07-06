```c++
#include <iostream>
#include <string>

int is_bored(std::string S) {
    int count = 0;
    size_t pos = 0;
    while ((pos = S.find("I", pos)) != std::string::npos) {
        if (S.find(".", pos) == std::string::npos && S.find("?", pos) == std::string::npos && S.find("!", pos) == std::string::npos)
            count++; // increment the counter
        else
            pos = S.find("I", pos + 1); // move the search to the next "I"
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