```c++
#include <iostream>
#include <string>

int is_bored(std::string input) {
    int count = 0;
    for(int i=0; i<input.length();i++) {
        if(input[i] == 'I' && !ispunct(input[i+1])) {
            count++;
        }
    }
    return count;
}

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);
    int result = is_bored(input);
    std::cout << "Number of 'I' without punctuation: " << result << "\n";
}