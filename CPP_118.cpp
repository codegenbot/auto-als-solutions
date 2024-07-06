```cpp
#include <iostream>
#include <string>
#include <cctype>

std::string get_closest_vowel(std::string str) {
    int closestVowelIndex = -1;
    for(int i=0; i<str.length(); i++) {
        char c = tolower(str[i]);
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            closestVowelIndex = i;
            break;
        }
    }
    if(closestVowelIndex != -1)
        return str.substr(closestVowelIndex, 1);
    else
        return "No vowel found";
}

int main() {
    std::string word;
    std::cout << "Enter a word: ";
    std::cin >> word;
    std::cout << "The closest vowel is: " << get_closest_vowel(word) << std::endl;
    return 0;
}