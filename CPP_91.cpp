```c++
#include <iostream>
#include <string>

int is_bored(std::string input);

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);
    int result = is_bored(input);
    std::cout << "Number of 'I' without punctuation: " << result << "\n";
}

int is_bored(std::string input) {
    int count = 0;
    for (char c : input) {
        if (c == 'I') {
            count++;
        }
    }
    return count;
}