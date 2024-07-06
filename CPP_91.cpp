```cpp
#include <iostream>
#include <string>

int is_bored(std::string S) {
    int count = 0;
    std::string::const_iterator pos = S.begin();
    while ((pos = S.find("I", pos)) != S.end()) {
        if (S.find(".", pos) == S.end() && S.find("?", pos) == S.end() && S.find("!", pos) == S.end())
            count++;
        else
            pos += S.find(".", pos, pos)+1;
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