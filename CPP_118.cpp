```cpp
#include <iostream>
#include <string>
#include <limits>

std::string get_closest_vowel(std::string str) {
    int min_dist = std::numeric_limits<int>::max();
    char closest_vowel = '\0';
    for (int i = 0; i < str.length(); i++) {
        if ((str[i] >= 'a' && str[i] <= 'z') || (str[i] >= 'A' && str[i] <= 'Z')) {
            int dist = i;
            if (dist < min_dist) {
                min_dist = dist;
                for (char c : "aeiouAEIOU") {
                    if (str[i] == c) {
                        closest_vowel = c;
                        break;
                    }
                }
            }
        }
    }
    return std::string(1, closest_vowel);
}

int main() {
    std::string word;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cout << "Enter a word: ";
    std::getline(std::cin, word);
    std::cout << "The closest vowel is: " << get_closest_vowel(word) << std::endl;
    return 0;
}