#include <iostream>
#include <vector>
#include <string>

// Convert the given input integer to a string
std::string intToString(int x) {
    std::string str = std::to_string(x);
    return str;
}

int main() {
    // Read user input as an integer
    int x; 
    std::cout << "Enter an integer: ";
    std::cin >> x;

    // Convert the integer to a string and then convert it to uppercase or lowercase according to the problem description.
    std::string str = intToString(x);
    if(str.size() % 2 == 0) {
        for(int i=0; i<str.size(); i++) {
            str[i] = toupper((unsigned char)str[i]);
        }
    } else {
        for(int i=0; i<str.size(); i++) {
            str[i] = tolower((unsigned char)str[i]);
        }
    }

    // Print the modified string
    std::cout << "Modified string: " << str << std::endl;

    return 0;
}