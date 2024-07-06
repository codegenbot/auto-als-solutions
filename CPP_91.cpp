```cpp
#include <iostream>
#include <string>

int is_bored(std::string S) {
    int count = 0;
    size_t pos = 0;
    while ((pos = S.find("I", pos)) != std::string::npos) {
        if (pos == S.find(".", pos) || pos == S.find("?", pos) || pos == S.find("!", pos))
            pos = S.find("I", pos + 1);
        else {
            size_t start_pos = S.find("I");
            while(start_pos != std::string::npos) {
                S.erase(start_pos, 1); // erase the found "I"
                start_pos = S.find("I"); // find next "I" to erase
            }
            count++;
        }
    }
    return count;

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);
    int result = is_bored(input);
    std::cout << "Number of 'I' without punctuation: " << result << "\n";
}