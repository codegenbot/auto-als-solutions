```cpp
#include <iostream>
#include <string>

std::string get_closest_vowel(std::string word) {
    std::string closest = "";
    for (char c : word) {
        if ("aeiouAEIOU".find(c) != std::string::npos) {
            if (closest.empty()) {
                closest = c;
            } else {
                return closest;
            }
        }
    }
    return closest;
}

int main() {
    std::string word;
    std::cout << "Enter a word: ";
    std::cin >> word;
    std::cout << "The closest vowel is: " << get_closest_vowel(word) << std::endl;
    // assert (get_closest_vowel("Above") == "o");
    return 0;
}